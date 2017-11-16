// A very wordy script to return the sum of a sequence. 
// After seeing the top rated answers on codewars I realized my method is quite silly.
// Refactor this 8-|

const sequenceSum = (begin, end, step) => {
	if (begin > end) {
		return 0;
	};
	let sum = begin; 
	if (end%step == 0) {
		while (true){
			if (begin >= end) {
				return sum;
			}
			sum += (begin+step);
			begin += step;
		}
	}
	else {
		while ((begin+step) <= end) {
			sum += (begin+step);
			begin += step;
		}
	}
	return sum;
}
