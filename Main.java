interface Operation {
	double PI = 3.14;
	double area();
	double volume();
	
}


class Circle1 implements Operation {
	private double radius;
	public Circle1 (double radius){
		this.radius = radius;

	}


	@Override
	public double area(){
		return PI * radius * radius;
	}

	@Override
	public double volume(){
		return 0;
	}
}

class Cylinder implements Operation {
	private double radius;
	private double height;
	
	public Cylinder (double radius, double height) {
		this.radius = radius;
		this.height = height;
	}

	@Override
	public double volume(){
		return PI * radius * radius * radius;
	}
	@Override
	public double area(){
		return 2*PI * radius * (radius + height);
	}
}



public class Main{
	public static void main(String[] args){
		// circle class obj
		Circle1 circle = new Circle1(5);
		System.out.println("Circle Area: " + circle.area());
		System.out.println("Circle Volume: " + circle.volume());

		// cylinder class obj
		Cylinder cylinder = new Cylinder(5, 7);
		System.out.println("Cylinder Volume: " + cylinder.volume());
		System.out.println("Cylinder Aera: " + cylinder.volume());
	}
}


