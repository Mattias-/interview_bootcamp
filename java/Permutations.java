package java_interview_bootcamp;

import java.util.LinkedList;
import java.util.List;

public class Permutations {

	public static void main(String[] args) {
		String s = "abcd";
		List<String> r1 = permutations(s);
		System.out.println(r1);
		List<String> r2 = permutations_recursive(s);
		System.out.println(r2);
	}

	public static List<String> permutations(String s) {
		List<String> prev_perms = new LinkedList<>();
		List<String> temp = new LinkedList<>();
		prev_perms.add(s.substring(0, 1));

		for (int i = 1; i < s.length(); i++) {
			temp = new LinkedList<>();
			for (String perm : prev_perms) {
				for (int j = 0; j <= perm.length(); j++) {
					String res = perm.substring(0, j) + s.substring(i, i + 1)
							+ perm.substring(j);
					temp.add(res);
				}
			}
			prev_perms = temp;
		}
		return prev_perms;
	}

	public static List<String> permutations_recursive(String s) {
		List<String> ret = new LinkedList<>();
		if (s.length() <= 1) {
			ret.add(s);
			return ret;
		}
		String first_char = s.substring(0, 1);
		List<String> permutations = permutations_recursive(s.substring(1));
		for (String perm : permutations) {
			for (int i = 0; i <= perm.length(); i++) {
				String p = perm.substring(0, i) + first_char
						+ perm.substring(i);
				ret.add(p);
			}
		}
		return ret;
	}

}
