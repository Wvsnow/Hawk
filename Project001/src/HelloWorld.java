// The note method

import java.util.*;

// import class FIR;

public class HelloWorld {
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		System.out.println("Hello£¬ YY.");
		System.out.println("Hello£¬ world.");
		System.out.println("");

		multiTable();
		addTable();

		// inputTest();
		newClass();

		System.out.println("End...");
	}

	public static void multiTable() {
		System.out.println("");
		int i = 0;
		int j = 0;
		for (i = 1; i < 10; i++) {
			for (j = 10 - i; j < 10; j++) {
				System.out.printf("%d * %d = %d  ", i, j, i * j);
				if (i * j < 10)
					System.out.print(" ");
			}
			System.out.println();
		}
		System.out.println("This is the multiplication table.");
		System.out.println();
	}

	public static void addTable() {
		System.out.println("");
		int i = 0;
		int j = 0;
		for (i = 0; i < 10; i++) {
			for (j = i; j < 10; j++) {
				System.out.printf("%d + %d = %d  ", i, j, i + j);
				if (i + j < 10)
					System.out.print(" ");
			}
			System.out.println();
		}
		System.out.println("This is the addation table.");
		System.out.println();
	}

	public static void inputTest() {

		Scanner in = new Scanner(System.in);

		System.out.println("Input one line ...");
		String ainput = in.nextLine();
		System.out.println(ainput);

		System.out.println("Input one string ...");
		String firststr = in.next();
		System.out.println(firststr);

		System.out.println("Input one number int ...");
		int num = in.nextInt();
		System.out.println(num);

		System.out.println("Input one number double ...");
		double adouble = in.nextDouble();
		System.out.println(adouble);

		System.out.println();
	}

	public static void newClass() {
		FIR.showDetail();
		FIR.showScaleInfo();

		FIR Fir01 = new FIR();
		Fir01.showInfo();

		FIR Fir02 = new FIR(10);
		Fir02.showInfo();

		FIR Fir03 = new FIR(1024, "Give you!");
		Fir03.showInfo();

		FIR fir = new FIR(16, "16 level fir filter.");
		fir.normalization();

		System.out.println();
	}

}
