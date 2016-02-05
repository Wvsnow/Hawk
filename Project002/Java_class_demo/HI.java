package ins.wvsen;

public class HI {

    public static void main(String[] args) {
        for (int i = 1; i < 16; i++) {
            System.out.println();
            for (int j = 1; j < i; j++) {
                System.out.print(i + "*" + j + "=" + i * j + "\t");
            }
        }
    }

}