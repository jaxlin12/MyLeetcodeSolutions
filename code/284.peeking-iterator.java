import java.util.Iterator;

/*
 * @lc app=leetcode id=284 lang=java
 *
 * [284] Peeking Iterator
 */

// @lc code=start
// Java Iterator interface reference:
// https://docs.oracle.com/javase/8/docs/api/java/util/Iterator.html

class PeekingIterator implements Iterator<Integer> {
	Iterator<Integer> myIterator;
	Integer last;

	public PeekingIterator(Iterator<Integer> iterator) {
	    // initialize any member here.
	    myIterator = iterator;
		if(iterator.hasNext()) {
			last = iterator.next();
		}
		else {
			last = null;
		}
	}
	
    // Returns the next element in the iteration without advancing the iterator.
	public Integer peek() {
        return last;
	}
	
	// hasNext() and next() should behave the same as in the Iterator interface.
	// Override them if needed.
	@Override
	public Integer next() {
		Integer ret;
		if (last == null) {
			return myIterator.next();
		}
		else {
			ret = last;
			if(myIterator.hasNext()) {
				last = myIterator.next();
			}
			else {
				last = null;
			}
		}
		return ret;
	}
	
	@Override
	public boolean hasNext() {
	    return last != null;
	}
}
// @lc code=end

