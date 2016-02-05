//: Garbage.java
// Demonstration of the garbage
// collector and finalization
class Chair {
	static boolean gcrun = false;
	static boolean f = false;
	static int created = 0;
	static int finalized = 0;
	volatile int i;

	Chair() {
		i = ++created;
		if (47 == created){
			System.out.println("Created 47");
		}else if(0 == created%50000){
			System.out.println("Created the "+created +"th object.");
		}
	}

	protected void finalize() {
		if (!gcrun) {
			gcrun = true;
			System.out.println("Beginning to finalize after " + created
					+ " Chairs have been created");
		}
		if (47 == finalized) {
			System.out.println("Finalizing Chair #47, "
					+ "Setting flag to stop Chair creation");
			f = true;
		}
		finalized++;
		if ((finalized >= created-5000 && 0 == finalized%500) || (finalized >= created-5)){
			System.out.println("All " + finalized + " finalized");
		}
		if(0 == finalized%50000){
			System.out.println("finalized the "+finalized +"th object. (Wiht"+created+" All.)");
		}
	}
}

public class Garbage {
	
	public static void main(String[] args) {
		if (args.length == 0) {
			System.err.println("Usage: \n" + "java Garbage before\n or:\n"
					+ "java Garbage after");
			return;
		}
		while (!Chair.f) {
			new Chair();
			new String("To take up space");
		}
		System.out.println("After all Chairs have been created:\n"
				+ "total created = " + Chair.created + ", total finalized(Currently) = "
				+ Chair.finalized);
		if (args[0].equals("before")) {
			System.out.println("gc():");
			System.gc();
			System.out.println("runFinalization():");
			System.runFinalization();
		}
		System.out.println("bye!");
		if (args[0].equals("after")){
			System.runFinalizersOnExit(true);
		}
		System.out.println("End of main-fun.");
	}
} // /:~