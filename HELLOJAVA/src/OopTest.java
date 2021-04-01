
public class OopTest {

	public static void main(String[] args) {
		Animal ani = new Animal();
		System.out.println(ani.age);
		ani.getOlder();
		System.out.println(ani.age);

		Human hum = new Human();
		System.out.println(hum.flag_coding);
		System.out.println(hum.age);
		hum.cutHand();
		hum.getOlder();
		System.out.println(hum.flag_coding);
		System.out.println(hum.age);
	}
}
