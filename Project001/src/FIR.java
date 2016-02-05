/*
<!--[if !supportLists]-->0. Ctrl + 1 （快速修复）
<!--[if !supportLists]-->1. Ctrl + D （删除当前行)
<!--[if !supportLists]-->2. Ctrl + Alt + ↓（复制当前行到下一行）
<!--[if !supportLists]-->3. Alt + / 或者说是 Ctrl + 空格（由于后者与输入法的快捷键冲突，所以，我一般都用前者） 作用：快速插入。
<!--[if !supportLists]-->4. Alt+Shift+R 重命名非常好用。
<!--[if !supportLists]-->5. Ctrl + Q 定位到最后编辑的地方。
<!--[if !supportLists]-->6. Ctrl + Shift + O 自动导入包。
<!--[if !supportLists]-->7. Ctrl+/ 注释当前行,再按则取消注释。[6] 
<!--[if !supportLists]-->8. Ctrl+K快速查找。
<!--[if !supportLists]-->9. Ctrl + Shift + F 自动缩进。

		Eclipse最全快捷键，熟悉快捷键可以帮助开发事半功倍，节省更多的时间来用于做有意义的事情。
	Ctrl+1  快速修复(最经典的快捷键,就不用多说了)
	Ctrl+D: 删除当前行
	Ctrl+Alt+↓ 复制当前行到下一行(复制增加)
	Ctrl+Alt+↑ 复制当前行到上一行(复制增加)
	Alt+↓ 当前行和下面一行交互位置(特别实用,可以省去先剪切,再粘贴了)
	Alt+↑ 当前行和上面一行交互位置(同上)
	Alt+← 前一个编辑的页面
	Alt+→ 下一个编辑的页面(当然是针对上面那条来说了)
	Alt+Enter 显示当前选择资源(工程,or 文件 or文件)的属性
	Shift+Enter 在当前行的下一行插入空行(这时鼠标可以在当前行的任一位置,不一定是最后)
	Shift+Ctrl+Enter 在当前行插入空行(原理同上条)
	Ctrl+Q 定位到最后编辑的地方
	Ctrl+L 定位在某行 (对于程序超过100的人就有福音了)
	Ctrl+M 最大化当前的Edit或View (再按则反之)
	Ctrl+/ 注释当前行,再按则取消注释
	Ctrl+O 快速显示 OutLine
	Ctrl+T 快速显示当前类的继承结构
	Ctrl+W 关闭当前Editer
	Ctrl+K 参照选中的Word快速定位到下一个
	Ctrl+E 快速显示当前Editer的下拉列表(如果当前页面没有显示的用黑体表示)
	Ctrl+/(小键盘) 折叠当前类中的所有代码
	Ctrl+×(小键盘) 展开当前类中的所有代码
	Ctrl+Space 代码助手完成一些代码的插入(但一般和输入法有冲突,可以修改输入法的热键,也可以暂用Alt+/来代替)
	Ctrl+Shift+E 显示管理当前打开的所有的View的管理器(可以选择关闭,激活等操作)
	Ctrl+J 正向增量查找(按下Ctrl+J后,你所输入的每个字母编辑器都提供快速匹配定位到某个单词,如果没
	有,则在stutes line中显示没有找到了,查一个单词时,特别实用,这个功能Idea两年前就有了)
	Ctrl+Shift+J 反向增量查找(和上条相同,只不过是从后往前查)
	Ctrl+Shift+F4 关闭所有打开的Editer
	Ctrl+Shift+X 把当前选中的文本全部变为大写
	Ctrl+Shift+Y 把当前选中的文本全部变为小写
	Ctrl+Shift+F 格式化当前代码
	Ctrl+Shift+P 定位到对于的匹配符(譬如{}) (从前面定位后面时,光标要在匹配符里面,后面到前面,则反之)
		下面的快捷键是重构里面常用的,本人就自己喜欢且常用的整理一下(注:一般重构的快捷键都是Alt+Shift开头的了)
	Alt+Shift+R 重命名 (是我自己最爱用的一个了,尤其是变量和类的Rename,比手工方法能节省很多劳动力)
	Alt+Shift+M 抽取方法 (这是重构里面最常用的方法之一了,尤其是对一大堆泥团代码有用)
	Alt+Shift+C 修改函数结构(比较实用,有N个函数调用了这个方法,修改一次搞定)
	Alt+Shift+L 抽取本地变量( 可以直接把一些魔法数字和字符串抽取成一个变量,尤其是多处调用的时候)
	Alt+Shift+F 把Class中的local变量变为field变量 (比较实用的功能)
	Alt+Shift+I 合并变量(可能这样说有点不妥Inline)
	Alt+Shift+V 移动函数和变量(不怎么常用)
	Alt+Shift+Z 重构的后悔药(Undo)[7] 

*/
public class FIR {
	static protected int MaxLevel = 2048;
	static private int MinLevel = 1;

	public int level;
	double paras[];
	public String describe;

	public FIR() {
		System.out.println("No parameter constructor funciton be called...");
		level = 1;
		paras = new double[level];
		describe = "Default";
	}

	public FIR(int level) {
		this.level = level;
		paras = new double[level];
		describe = "Default";
		System.out.println("One parameter constructor funciton be called...");
	}

	public FIR(int level, String str) {
		System.out.println("Two parameter constructor funciton be called...");
		this.level = level;
		paras = new double[level];
		this.describe = str;
	}

	public void showInfo() {
		System.out
				.println("The current class instance wiht the following information: ");
		System.out.printf("level  = %d;\ndescricbe = %s;\n", level, describe);
		if (null != this.paras) {
			System.out.printf("Parameters are not empty, and with: ");
			if (level == 1) {
				System.out.printf("paras[%d] = %f.", level - 1,
						paras[level - 1]);
			} else if (2 == level) {
				System.out.printf("paras[0] = %f;paras[%d] = %f.", paras[0],
						level - 1, paras[level - 1]);
			} else {
				System.out
						.printf("paras[0] = %f;...;paras[%d] = %.2f;...;paras[%d] = %f.",
								paras[0], level / 2, paras[level / 2],
								level - 1, paras[level - 1]);
			}
		} else {
			System.out.println("...");
		}
		System.out.println();
		System.out.println();
	}

	public boolean normalization() {
		double sum = 0.0;
		for (int i = 0; i < level; i++) {
			sum += paras[i];
		}
		if (sum < Double.MIN_VALUE) {

		}
		if (sum == 0.0) {
			System.out.println("sum = 0(The real zero)");
		} else {
			System.out.printf("sum = %lf(Not the real zero)", sum);
		}
		return true;

	}

	static void showScaleInfo() {
		System.out.println("Integer.MIN_VALUE = " + Integer.MIN_VALUE);
		System.out.println("Integer.MAX_VALUE = " + Integer.MAX_VALUE);

		System.out.println("Long.MIN_VALUE = " + Long.MIN_VALUE);
		System.out.println("Long.MAX_VALUE = " + Long.MAX_VALUE);

		System.out.println("Float.MIN_VALUE = " + Float.MIN_VALUE);
		System.out.println("Float.MIN_NORMAL = " + Float.MIN_NORMAL);
		System.out.println("Float.MAX_VALUE = " + Float.MAX_VALUE);

		System.out.println("Double.MAX_VALUE = " + Double.MAX_VALUE);
		System.out.println("Double.MIN_VALUE = " + Double.MIN_VALUE);
	}

	static void showDetail() {
		System.out.println("The current class wiht the following detail: ");
		System.out.printf("minimum level  = %d; maximum level = %d.\n",
				MinLevel, MaxLevel);
		System.out.println();
		System.out.println();
	}

}
