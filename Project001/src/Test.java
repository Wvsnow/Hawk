import java.util.ArrayList;
import java.util.Date;
import java.util.concurrent.Callable;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Future;
import java.text.SimpleDateFormat;

import java.util.concurrent.*;
import java.util.List;
import java.util.*;

public class Test {

	/*
	 * Test 001
	 */

	static void showSelf() {
		SimpleDateFormat df = new SimpleDateFormat("yyyy-MM-dd HH:mm:ss");
		System.out.println(df.format(new Date()));
	}

	public static void main(String[] args) {
		showSelf();

		TestThread myThread1 = new TestThread();
		TestThread myThread2 = new TestThread();
		myThread1.start();
		myThread2.start();

		int[] a1 = { 1, 2, 3, 4, 5 };
		int[] a2;
		a2 = a1;
		for (int i = 0; i < a2.length; i++) {
			a2[i]++;
		}
		for (int i = 0; i < a1.length; i++){
			prt("a1[" + i + "] = " + a1[i]);
		}
	
		Vector v = new Vector();
		for (int i = 0; i < 5; i++) {
			v.addElement(new Test());
		}
		System.out.println(v);
		


		
	}

	static void prt(String s) {
		System.out.println(s);
	}

	// /*
	// * Test 002
	// *
	// */
	// public static void main(String[] args) throws ExecutionException,
	// InterruptedException {
	// System.out.println("----App Start----");
	// Date date1 = new Date();
	//
	// int taskSize = 5;
	// // ����һ���̳߳�
	// ExecutorService pool = Executors.newFixedThreadPool(taskSize);
	// // ��������з���ֵ������
	// List<Future> list = new ArrayList<Future>();
	// for (int i = 0; i < taskSize; i++) {
	// Callable c = new MyCallable(i + " ");
	// // ִ�����񲢻�ȡFuture����
	// Future f = pool.submit(c);
	// // System.out.println(">>>" + f.get().toString());
	// list.add(f);
	// }
	// // �ر��̳߳�
	// pool.shutdown();
	//
	// // ��ȡ���в�����������н��
	// for (Future f : list) {
	// // ��Future�����ϻ�ȡ����ķ���ֵ�������������̨
	// System.out.println(">>>" + f.get().toString());
	// }
	//
	// Date date2 = new Date();
	// System.out.println("----�����������----����������ʱ�䡾"
	// + (date2.getTime() - date1.getTime()) + "���롿");
	// }

}

class MyCallable implements Callable<Object> {
	private String taskNum;

	MyCallable(String taskNum) {
		this.taskNum = taskNum;
	}

	public Object call() throws Exception {
		System.out.println(">>>" + taskNum + "��������");
		Date dateTmp1 = new Date();
		Thread.sleep(1000);
		Date dateTmp2 = new Date();
		long time = dateTmp2.getTime() - dateTmp1.getTime();
		System.out.println(">>>" + taskNum + "������ֹ");
		return taskNum + "���񷵻����н��,��ǰ����ʱ�䡾" + time + "���롿";
	}
}

//
// public class MyRunnable implements Runnable() {
// public void run() {
// methodOne();
// }
// public void methodOne() {
// int localVariable1 = 45;
// MySharedObject localVariable2 =
// MySharedObject.sharedInstance;
// //... do more with local variables.
// methodTwo();
// }
// public void methodTwo() {
// Integer localVariable1 = new Integer(99);
// //... do more with local variable.
// }
// }
// public class MySharedObject {
// //static variable pointing to instance of MySharedObject
// public static final MySharedObject sharedInstance =
// new MySharedObject();
// //member variables pointing to two objects on the heap
// public Integer object2 = new Integer(22);
// public Integer object4 = new Integer(44);
// public long member1 = 12345;
// public long member1 = 67890;
// }
//
