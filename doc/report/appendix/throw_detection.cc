while (!throw_end) {

	pBufferFilled = pDataStream->GetFilledBuffer(15); // 15 ms timeout

	if (pBufferFilled == NULL) {
		// 15 ms buffer timeout (loss of 3 frames @ 200 fps)
	} else if (pBufferFilled->GetIsIncomplete() == true) {
		// Image incomplete, queue buffer again
		pBufferFilled->QueueBuffer();
	} else {

		// OpenCV matrix with Baumer BayerRG8 (OpenCV BayerBG) pixel format
		cv_buffer[frame_id % buff_size] = cv::Mat(height, width, CV_8UC1, (void *)pBufferFilled->GetMemPtr());

		if (frame_id != 0) { // Skip the first frame

			// Compute the mean pixel difference
			cv::absdiff(cv_buffer[frame_id % buff_size], cv_buffer[(frame_id - 1) % buff_size], cv_abs);(*\label{lst:ln:abs_diff}*)
			mean_diff = cv::sum(cv_abs)[0] / (width * height);(*\label{lst:ln:mean_diff}*)

			// Average diffs over (`avg_diffs` + 1) frames
			if (frame_id < avg_diffs) {
				sum_thresh += mean_diff;
			} else if (frame_id == avg_diffs) {
				sum_thresh += mean_diff;
				threshold = sum_thresh / avg_diffs * threshold_mult;
			} else {
				// Detect throw
				if (mean_diff >= threshold) {
					if (!throw_bgn) {
						throw_bgn_idx = frame_id;
						throw_bgn = true;
					}
				} else {
					if (throw_bgn) {
						throw_end_idx = frame_id;

						// Remove glitches (single frame changes)
						if ((throw_end_idx - throw_bgn_idx) == 1) {
							throw_bgn = false;
						} else {
							throw_end = true;
						}
					}
				}
			}

		}

		++frame_id;

		// If no throw is detected, release the Buffer
		if (!throw_bgn) {
			pBufferFilled->QueueBuffer();
		}

	}
}
