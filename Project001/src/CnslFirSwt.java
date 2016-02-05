import java.awt.Graphics;
import java.awt.Font;
import java.awt.Point;
import java.awt.Rectangle;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.io.BufferedWriter;
import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileWriter;
import java.io.IOException;
import java.util.List;
import java.util.ArrayList;
import java.util.Iterator;
import java.util.Scanner;

import javax.swing.JButton;
import javax.swing.JFileChooser;
import javax.swing.JFrame;
//import javax.swing.JPanel;
//import javax.swing.JScrollPane;
import javax.swing.JTextArea;
import javax.swing.JTextField;
import javax.swing.filechooser.FileNameExtensionFilter;
import javax.swing.text.Utilities;

public class CnslFirSwt {
	public static void main(String[] args) {
		MyFrame temp = new MyFrame();
		temp.setBounds(10, 10, 1200, 800);
	}
}

class MyFrame extends JFrame implements ActionListener {

	/**
	 * 
	 */
	private static final long serialVersionUID = 1L;

	private JButton button1;
	private JButton button2;
	private JButton button3;
	private JButton button4;
	private JButton button5;

	private JButton exchangeBnt;
	private JButton multiThreadBnt;

	private JTextField text1;
	private JTextField text2;
	private JTextField text3;

	private JTextArea textField1;
	private JTextArea textField2;
	private JTextArea area;
	private JTextArea multiThreadarea;

	public MyFrame() {
		setTitle("JAVA SWT test");
		setLayout(null);
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setBounds(10, 10, 900, 600);
		setVisible(true);

		init();
	}

	private void init() {
		initButtons();
		initTextField();
		initTextArea();

		initVisible();
	}

	private void initVisible() {
		boolean isVis = false;
		if (isVis) {
			textField1.setVisible(false);
			textField2.setVisible(false);
			area.setVisible(false);

			multiThreadBnt.setVisible(true);
			multiThreadarea.setVisible(true);

		} else {
			textField1.setVisible(true);
			textField2.setVisible(true);
			area.setVisible(true);

			multiThreadBnt.setVisible(false);
			multiThreadarea.setVisible(false);
		}
	}

	private void initButtons() {
		// Buttons
		button1 = new JButton("Open the 1st file.");
		button2 = new JButton("Open the 2nd file.");
		button3 = new JButton("Open the 3rd file.");
		button4 = new JButton("MERGE");
		button5 = new JButton("SHOW");

		int btnWidth = 240;
		int btnHeight = 24;
		int btnDeltaY = 30;
		Point btnSpnt = new Point(50, 20);
		Rectangle rectBtn = new Rectangle(btnSpnt.x, btnSpnt.y, btnWidth,
				btnHeight);
		button1.setBounds(rectBtn);
		rectBtn.y += btnDeltaY;
		button2.setBounds(rectBtn);
		rectBtn.y += btnDeltaY;
		button3.setBounds(rectBtn);
		rectBtn.y += btnDeltaY;
		button4.setBounds(rectBtn);
		rectBtn.y += btnDeltaY;
		button5.setBounds(rectBtn);

		button1.addActionListener(this);
		button2.addActionListener(this);
		button3.addActionListener(this);
		button4.addActionListener(this);
		button5.addActionListener(this);

		add(button1);
		add(button2);
		add(button3);
		add(button4);
		add(button5);

		exchangeBnt = new JButton("Exchange State");
		multiThreadBnt = new JButton("Multi-Thread");
		rectBtn.y -= 1 * btnDeltaY;
		rectBtn.x += btnWidth + btnDeltaY;
		rectBtn.height = 55;
		rectBtn.width = 150;
		exchangeBnt.setBounds(rectBtn);
		rectBtn.x += btnDeltaY + rectBtn.width;
		multiThreadBnt.setBounds(rectBtn);
		exchangeBnt.addActionListener(this);
		multiThreadBnt.addActionListener(this);
		add(exchangeBnt);
		add(multiThreadBnt);
	}

	private void initTextField() {
		// Text labels field
		int labelWidth = 600;
		int labelHeight = 22;
		int labelDeltaY = 30;
		Point labelSpnt = new Point(300, 20);
		Rectangle rectlabel = new Rectangle(labelSpnt.x, labelSpnt.y,
				labelWidth, labelHeight);

		text1 = new JTextField();
		text1.setBounds(rectlabel);
		rectlabel.y += labelDeltaY;
		text2 = new JTextField();
		text2.setBounds(rectlabel);
		rectlabel.y += labelDeltaY;
		text3 = new JTextField();
		text3.setBounds(300, 80, 600, 20);

		text1.setText("A...A");
		text2.setText("B......B");
		text3.setText("C.........C");
		text1.setHorizontalAlignment(JTextField.LEFT);
		text2.setHorizontalAlignment(JTextField.CENTER);
		text3.setHorizontalAlignment(JTextField.RIGHT);
		Font fontCurr = new Font("Times New Roman", 0, 16);
		text1.setFont(fontCurr);

		add(text1);
		add(text2);
		add(text3);
	}

	private void initMultiThreadTextArea() {
		Point sPnt = new Point(0, 0);
		sPnt.x = 40;
		sPnt.y = 180;
		int deltaX = 800 / 1;
		int deltaXSpace = 60 / 3;
		int height = 600;
		Rectangle rect = new Rectangle();
		rect.x = 100;
		rect.y = 300;
		rect.width = 800;
		rect.height = 400;
		rect.setBounds(sPnt.x, sPnt.y, deltaX, height);

		multiThreadarea = new JTextArea(1, 5);
		multiThreadarea.setBounds(rect);
		multiThreadarea.setText("start..A......Z...end");
		for (int i = 0; i < 12; i++) {
			multiThreadarea
					.append("The deepest stars sky and the human soul...\n");
		}
		add(multiThreadarea);
	}

	private void initTextArea() {
		// Text area
		Point sPnt = new Point(0, 0);
		sPnt.x = 40;
		sPnt.y = 180;
		int deltaX = 900 / 3;
		int deltaXSpace = 60 / 3;
		int height = 500;
		Rectangle rect = new Rectangle();
		rect.x = 100;
		rect.y = 300;
		rect.width = 800;
		rect.height = 400;

		rect.setBounds(sPnt.x, sPnt.y, deltaX, height);
		textField1 = new JTextArea(1, 5);
		textField1.setBounds(rect);
		textField1.setText("start..A......Z...end");
		for (int i = 0; i < 16; i++) {
			textField1.append("The deepest stars sky and the human soul...\n");
		}

		rect.x += deltaX + deltaXSpace;
		textField2 = new JTextArea(1, 5);
		textField2.setBounds(rect);
		textField2.setText("start..A......Z...end");
		for (int i = 0; i < 20; i++) {
			textField2.append("walking down the same old street...\n");
		}

		rect.x += deltaX + deltaXSpace;
		area = new JTextArea();
		area.setBounds(rect);
		area.setText("start..A......Z...end");
		for (int i = 0; i < 26; i++) {
			area.append("You are the world, you are the god...\n");
		}

		add(textField1);
		add(textField2);
		add(area);

		initMultiThreadTextArea();
	}

	public void actionPerformed(ActionEvent e) {

		String currDir = "E:\\Application\\AndroidPrograms\\Eclipse\\workspace\\RootSource";
		File currFile = new File(currDir);
		FileNameExtensionFilter filterTXTOnly = new FileNameExtensionFilter(
				"TXT Document", "txt");

		// JFileChooser chooser = new JFileChooser(currFile);
		// FileNameExtensionFilter filter = new FileNameExtensionFilter(
		// "JPG & GIF Images", "jpg", "gif");
		// chooser.setFileFilter(filter);
		// int returnVal = chooser.showOpenDialog(this);
		// if(returnVal == JFileChooser.APPROVE_OPTION) {
		// System.out.println("You chose to open this file: " +
		// chooser.getSelectedFile().getName());
		// }

		if (e.getSource() == button1) {
			JFileChooser f = new JFileChooser(currFile);
			f.setFileFilter(filterTXTOnly);
			int retVal = f.showDialog(this, "Open the 1st File to be merged");
			if (retVal == JFileChooser.APPROVE_OPTION) {
				System.out.println("You chose to open this file: "
						+ f.getSelectedFile().getName());
				text1.setText(f.getSelectedFile().getPath());
				textField1.setText(getData("", text1.getText()));
			} else {
				System.out.println("Unavailiable file direciton.");
			}
		} else if (e.getSource() == button2) {
			JFileChooser f = new JFileChooser(currFile);
			f.setFileFilter(filterTXTOnly);
			int retVal = f.showDialog(this, "Open the 2nd File to be merged");
			if (retVal == JFileChooser.APPROVE_OPTION) {
				System.out.println("You chose to open this file: "
						+ f.getSelectedFile().getName());
				text2.setText(f.getSelectedFile().getPath());
				textField2.setText(getData("", text2.getText()));
			} else {
				System.out.println("Unavailiable file direciton.");
			}
		} else if (e.getSource() == button3) {
			JFileChooser f = new JFileChooser(currFile);
			f.setFileFilter(filterTXTOnly);
			int retVal = f.showDialog(this,
					"Open the 3rd File to merging which is the target");
			if (retVal == JFileChooser.APPROVE_OPTION) {
				System.out.println("You chose to open this file: "
						+ f.getSelectedFile().getName());
				text3.setText(f.getSelectedFile().getPath());
				area.setText(getData("", text3.getText()));
			} else {
				System.out.println("Unavailiable file direciton.");
			}
		} else if (e.getSource() == button4) {

			// File f1 = new File(text1.getText());
			// File f2 = new File(text2.getText());

			String result = "";
			result = getData(result, text1.getText());
			result = getData(result, text2.getText());
			saveData(result, text3.getText());
		} else if (e.getSource() == button5) {
			area.setText(getData("", text3.getText()));
		} else if (e.getSource() == exchangeBnt) {
			if (area.isVisible()) {
				textField1.setVisible(false);
				textField2.setVisible(false);
				area.setVisible(false);

				multiThreadBnt.setVisible(true);
				multiThreadarea.setVisible(true);

				// ArrayList currArrLst = dataGenerator();
				// Iterator iter = currArrLst.iterator();

				// double series1[] = iter.();
				// while(iter != null){
				// System.out.println(iter.toString());
				// iter.next();
				// }
				// System.out.println(iter.toString());
				// currArrLst.forEach(action);
				// forEach()

			} else {
				textField1.setVisible(true);
				textField2.setVisible(true);
				area.setVisible(true);

				multiThreadBnt.setVisible(false);
				multiThreadarea.setVisible(false);
			}
		} else if (e.getSource() == multiThreadBnt) {
			multiThreadTest();
		}
	}

	private String getData(String result, String path) {
		try {
			Scanner in = new Scanner(new File(path));
			while (in.hasNextLine()) {
				result += in.nextLine() + "\r\n";
			}
			in.close();
		} catch (FileNotFoundException e) {
			e.printStackTrace();
		}
		return result;
	}

	private void saveData(String result, String path) {
		try {
			BufferedWriter bw = new BufferedWriter(new FileWriter(
					new File(path)));
			bw.write(result);
			bw.flush();
			bw.close();
		} catch (IOException e) {
			e.printStackTrace();
		}
	}

	private ArrayList dataGenerator() {
		double series1[] = new double[5];
		for (int i = 0; i < series1.length; i++)
			series1[i] = (i * 10) + 10; // a linear series containing
										// 10,20,30,40,50

		double series2[] = new double[9];
		series2[0] = 20;
		series2[1] = 150;
		series2[2] = 5;
		series2[3] = 90;
		series2[4] = 35;
		series2[5] = 20;
		series2[6] = 150;
		series2[7] = 5;
		series2[8] = 45;

		double series3[] = new double[7];
		for (int i = 0; i < series3.length; i++) {
			series3[i] = (i * 20) + 15;
		}
		ArrayList seriesData = new ArrayList();
		seriesData.add(series1);
		seriesData.add(series2);
		seriesData.add(series3);
		return seriesData;
	}

	private int[] getXCoordinates(ArrayList seriesData) {
		int xSpan = (int) GraFixConstants.xSpan;
		int longestSeries = Utilities.getLongestSeries(seriesData);
		int numSegments = ((double[]) seriesData.get(longestSeries)).length;
		int sectionWidth = (int) xSpan / numSegments; // want to divide span of
														// xAxis

		int xPositions[] = new int[numSegments]; // will contain X-coordinate of
													// all dots.
		for (int i = 0; i < numSegments; i++) {
			xPositions[i] = (i + 1) * sectionWidth;// dots spaced at distance of
													// sectionWidth
		}
		return xPositions;
	}

	private void multiThreadTest() {
		System.out.println("Enter the multi-thread test function...");

		// List<MyThread> listThread01 = new List<MyThread>();

		MyThread thread01001 = new MyThread(100);
		thread01001.start();
		try {
			Thread.sleep(5);
		} catch (InterruptedException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		MyThread thread01002 = new MyThread(1000);
		thread01002.start();
		try {
			Thread.sleep(3);
		} catch (InterruptedException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		MyThread thread01003 = new MyThread(10000);
		thread01003.start();

		
		RunThreadTest thread201 = new RunThreadTest(200);
		for (int i = 0; i < 3; i++) {
			Thread thread02001 = new Thread(thread201,"Runable first instacne");
			thread02001.start();
		}
		try {
			Thread.sleep(5);
		} catch (InterruptedException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		RunThreadTest thread202 = new RunThreadTest(2000);
		for (int i = 0; i < 3; i++) {
			Thread thread02001 = new Thread(thread202,"Runable second instacne");
			thread02001.start();
		}
	}

}










class MyThread extends Thread {
	public static long count = 0;
	public int x = 0;
	public long currCount = 0;
	MyThread(int initialVal) {
		x = initialVal;
		currCount = count;
		count++;
	}

	MyThread() {
		x = 0;
		currCount = count;
		count++;
	}

	public void run() {
		System.out.printf(">>>thread 001 ID=%d(Total %d), wiht y = %5d\n", currCount, count, ++x);
		for (int i = 0; i < 10; i++) {
			System.out
					.printf(">>>thread 001 ID=%d(Total %d), wiht y = %5d\n", currCount, count, ++x);
			try {
				Thread.sleep((int) (Math.random() * 100) % 10);
			} catch (InterruptedException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			}
		}
	}
	
	public void run(String directory) {
		System.out.printf(">>>thread 001 ID=%d(Total %d), wiht y = %5d\n", currCount, count, ++x);
		for (int i = 0; i < 10; i++) {
			System.out
					.printf(">>>thread 001 ID=%d(Total %d), wiht y = %5d\n", currCount, count, ++x);
			try {
				Thread.sleep((int) (Math.random() * 100) % 10);
			} catch (InterruptedException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			}
		}
	}
	
}


class RunThreadTest implements Runnable {
	public static long count = 0;
	private int x = 0;
	public long currCount = 0;
	RunThreadTest(int initialVal) {
		x = initialVal;
		currCount = count;
		count++;
	}

	RunThreadTest() {
		x = 0;
		currCount = count;
		count++;
	}

	public void setVale(int value) {
		x = value;
	}

	public void run() {
		System.out
				.printf("~~~~~~~~~~~~~~~~~~~~~~~~~~~<<<thread 002 ID=%d(Total %d), wiht x = %5d\n",
						currCount, count, ++x);
		for (int i = 0; i < 10; i++) {
			System.out
					.printf("~~~~~~~~~~~~~~~~~~~~~~~~~~~<<<thread 002 ID=%d(Total %d), wiht x = %5d\n",
						currCount, count, ++x);
			try {
				Thread.sleep((int) (Math.random() * 100) % 10);
			} catch (InterruptedException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			}
		}
	}
}































