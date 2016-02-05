//package com.carefree;
// Simple App to analysis the code number. Too simple to be used practically!

import java.io.BufferedReader;
import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;

public class CodeCounter {

    /**
	 * wuhongsheng_2005@sina.com
	 * 此程序用于计算代码行数
    */
	
	static long codeLines = 0;
	static long commentLines = 0;
	static long spaceLines = 0;
	static long classnum = 0;
	static long num = 0;
	
	public static void main(String[] args) {
		
		File f = new File("E:\\Application\\AndroidPrograms\\Eclipse\\workspace\\MineFirCnsl\\src\\CodeCounter.java");	//这里的目录要输入你要统计代码的文件夹目录
		if(f.exists()) {
			judge(f);			
		}
				
		System.out.println("实际代码行数为："+codeLines);
		System.out.println("注释代码行数为："+commentLines);
		System.out.println("空行行数为："+spaceLines);
		num = codeLines+commentLines+spaceLines;
		System.out.println("总的行数为："+num);
		System.out.println("类的数目为："+classnum);
	}
	
	private static void judge(File f) {
		if(!f.isFile()) {
			File[] fs = f.listFiles();
			for(File child: fs) {
				judge(child);
			}
		}
		if(f.exists()&&f.isFile()) {
			counter(f);
		}
	}

	private static void counter(File child) {
		
		FileReader fr;
		try {
			fr = new FileReader(child);
			BufferedReader br = new BufferedReader(fr);
			String line = "";
			boolean flag = false;
			if(child.getName().matches(".*java$")) {
				try {
					while((line=br.readLine())!=null) {
						String l = line.trim();
						if(l.matches(".*class.+")) {
							classnum++;
						}
						if(l.matches("^[[\\s]&&[^\\n]]*")) {
							spaceLines++;
						}
						else if(l.startsWith("/*")&&l.endsWith("*/")) {
							commentLines++;
							flag = false;
						}
						else if(l.startsWith("/*")) {
							commentLines++;
							flag = true;
						}
						else if(l.endsWith("*/")) {
							commentLines++;
							flag = false;
						}
						else if(true == flag) {
							commentLines++;
						}
						else if(l.startsWith("//")) {
							commentLines++;
						}
						else {
							codeLines++;
						}
					}
				} catch (IOException e) {
					e.printStackTrace();
				}
			}
		} catch (FileNotFoundException e) {
			e.printStackTrace();
		}
	}

	
}