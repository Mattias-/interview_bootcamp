package java_interview_bootcamp;

public class ArrayList<E> {
	private final static int INITIAL_CAPACITY = 10;
	private int size = 0;
	private int capacity = INITIAL_CAPACITY;
	private E[] array;

	@SuppressWarnings("unchecked")
	public ArrayList() {
		this.array = (E[]) new Object[INITIAL_CAPACITY];
	}

	public void add(E element, int index) {
		if (index < 0 || index > size) {
			throw new IndexOutOfBoundsException();
		}
		if (this.size >= this.capacity) {
			this.grow();
		}
		for (int i = this.size; i > index; i--) {
			this.array[i] = this.array[i - 1];
		}
		this.array[index] = element;
		this.size++;
	}

	public void add(E element) {
		this.add(element, size);
	}

	public E remove(int index) {
		if (index < 0 || index >= size) {
			throw new IndexOutOfBoundsException();
		} else {
			E value = this.array[index];
			for (int i = index; i < this.size - 1; i++) {
				this.array[i] = this.array[i + 1];
			}
			this.size--;
			return value;
		}
	}

	public E get(int index) {
		if (index < 0 || index >= size) {
			throw new IndexOutOfBoundsException();
		} else {
			return this.array[index];
		}
	}

	public void swap(int i1, int i2) {
		if (i1 < 0 || i1 >= size) {
			throw new IndexOutOfBoundsException();
		}
		if (i2 < 0 || i2 >= size) {
			throw new IndexOutOfBoundsException();
		}
		E temp = this.array[i1];
		this.array[i1] = this.array[i2];
		this.array[i2] = temp;
	}

	public int getSize() {
		return size;
	}

	@SuppressWarnings("unchecked")
	private void grow() {
		E[] temp = (E[]) new Object[2 * this.capacity];
		for (int i = 0; i < this.size; i++) {
			temp[i] = this.array[i];
		}
		this.array = temp;
		this.capacity = 2 * this.capacity;
		// this.array = Arrays.copyOf(this.array, this.capacity);
	}

	public String toString() {
		StringBuilder sb = new StringBuilder();
		sb.append("[");
		for (int i = 0; i < this.size; i++) {
			sb.append(this.array[i]);
			if (i < this.size - 1) {
				sb.append(" -> ");
			}
		}
		sb.append("]");
		return sb.toString();
	}

	public static void main(String[] args) {
		ArrayList<Integer> al = new ArrayList<>();
		for (int i = 0; i < 20; i++) {
			al.add(i);
		}
		System.out.println(al.toString());
		al.add(333, 3);
		System.out.println(al.toString());
		System.out.println("Removed: " + al.remove(5));
		System.out.println(al.toString());
		al.swap(0, 1);
		System.out.println(al.toString());
	}

}
