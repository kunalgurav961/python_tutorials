 class Employee{
	String name;
	double salary;

	public Employee(String name, double salary){
		this.name = name;
		this.salary = salary;
	}

	public void displayEmpDetails(){
		System.out.println("Name: " + this.name + "\nSalary: " + this.salary);
	}
}



 class Developer extends Employee{
	String proj_name;

	public Developer(String name, double salary, String proj_name){
		super(name, salary);
		this.proj_name = proj_name;
	}

	public void displayDevDetails(){
		System.out.println("Name: " + this.name + "\nSalary: " + this.salary + "\nProjectName: " + this.proj_name);
	}
}

 class Programmer extends Developer{
	String prog_lang;

	public Programmer(String name, double salary, String proj_name, String prog_lang){
		super(name, salary, proj_name);
		this.prog_lang = prog_lang;
	}

	public void displayProDetails(){
		System.out.println("Name: " + this.name + "\nSalary: " + this.salary + "\nProjectName: " + this.proj_name + "\nProgramming Language: " + this.prog_lang);
	}
}


public class Main{
	public static void main(String[] args){
		Programmer kunal = new Programmer("Kunal Gurav", 1000000, "Portfolio", "Python");

		kunal.displayProDetails();
	}
}
