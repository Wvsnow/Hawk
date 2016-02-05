

import java.util.Scanner;


public class CnslSecApp {

	
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		System.out.println("Input a decimal integer number...");               
		int mark;          
		Scanner scanner = new Scanner(System.in);
		boolean isLegalInput = true;
		while( isLegalInput){
			System.out.println("Input a negative decimal integer number to exit...");
			mark = scanner.nextInt();
			if( mark >= 0){
				outputMultiTable(mark);
			}else{
				break;
			}
		}
		System.out.println("App is exit...");
	}
	
	
	public static void outputMultiTable( int mark) {
		if( mark < 0){
			System.out.println("Illegal input number..."); 
		}
		if( mark>16){
			mark = 16;
			System.out.println("Just show the first " + mark + "..."); 
		}
		mark ++;
		for (int j=0;j<mark;j++){
			for(int k=0;k<=j;k++){
				System.out.print(" "+k+"X"+j+"="+j*k); 
			} 
			System.out.println(); 
		}
	}

	
}
