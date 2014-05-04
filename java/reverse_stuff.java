package java_interview_bootcamp;

public class reverse_stuff {

	public static void main(String[] args) {
		String s = "race car";
		String s2 = "1234567";
		String res = reverse_string(s2);
		System.out.println(res);

		int[] int_a = { 1, 2, 3, 4, 5 };
		reverse_array_inplace(int_a);
		for (int i = 0; i < int_a.length; i++) {
			System.out.println(int_a[i]);
		}
	}

	public static String reverse_string(String s) {
		StringBuilder sb = new StringBuilder();
		for (int i = s.length() - 1; i >= 0; i--) {
			sb.append(s.charAt(i));
		}
		return sb.toString();
	}

	public static void reverse_array_inplace(int[] a) {
		int size = a.length - 1;
		for (int i = size / 2; i >= 0; i--) {
			int temp = a[i];
			a[i] = a[size - i];
			a[size - i] = temp;
		}
	}

}
