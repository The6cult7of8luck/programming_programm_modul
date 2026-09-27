#include <iostream>


using namespace std;

int quest1() {
	cout << "Hello world!!!";
	return 0;
}

int quest2() {
	int a, b;
	cout << "Введите первое число: ";
	cin >> a;
	cout << "Введите второе число: ";
	cin >> b;
	cout <<"Ответ: " << a <<" + "<< b <<" = " << a + b;
	return 0;
}

int quest3() {
	int a, b;
	cout << "Введите первое число: ";
	cin >> a;
	cout << "Введите второе число: ";
	cin >> b;
	cout << "Ответ: \n" << "Сумма: " << a+b;
	cout << "\nРазность (первое - второе): " << a - b;
	cout << "\nПроизведение: " << a * b;
	cout << "\nЦелое от деления на второе число: " << a / b;
	cout << "\nОстаток от деления на второе число: " << a % b;
	return 0;
}

int quest4() {
	float a, b;
	cout << "Введите первое число: ";
	cin >> a;
	cout << "Введите второе число: ";
	cin >> b;
	cout << "Ответ:\n Периметр: " <<(a+b)*2 << "\nПлощадь: "<< a*b;
	return 0;
}

int quest5() {
	float a, b, c;
	cout << "Введите первое число: ";
	cin >> a;
	cout << "Введите второе число: ";
	cin >> b;
	cout << "Введите третье число: ";
	cin >> c;
	cout << "Ответ:\n Среднее арифметическое: " << (a + b + c) / 3.0;
	return 0;
}

int quest6() {
	int a;
	cout << "Введите кол-во секунд: ";
	cin >> a;
	cout << "Ответ: " << a/3600 <<":" << (a % 3600) / 60 <<":" << a % 60;
	return 0;
}


int quest7() {
	float a;
	cout << "Введите температуру в градусах цельсия: ";
	cin >> a;
	cout << "Ответ: " << (a * 9.0) / 5.0 + 32.0;
	return 0;
}

int quest8() {
	double a;
	const double pi = 3.14159;
	cout << "Введите радиус круга: ";
	cin >> a;
	cout << "Ответ: \nДлинна окружности: " <<2.0*pi*a <<"\nПлощадь круга: "<<pi*a*a;
	return 0;
}

int quest9() {
	short a, b, c, d;
	cout << "Введите четырёхзначное число: ";
	cin >> a;
	d = a % 10;
	c = (a % 100) / 10;
	b = (a % 1000) / 100;
	a = a / 1000;
	cout << "Ответ: \nСумма цифр числа: "<< a+b+c+d<< "\nПроизведение цифр числа: " <<a*b*c*d;
	return 0;
}

int quest10() {
	short a, b, c;
	cout << "Введите почасавую ставку: ";
	cin >> a;
	cout << "Введите кол-во часов: ";
	cin >> b;
	cout << "Введите премию: ";
	cin >> c;
	const double nalog = 0.13;
	cout << "Ответ: \nНачислено: " << (a*b)+c << "\nНалог: " << ((a * b) + c)*nalog <<"\nНа руки: "<< ((a * b) + c)- ((a * b) + c) * nalog;
	return 0;
}

int quest11() {
	short num2, num3, num4, num5, num6, num7, num8, num9;
	int num1;
	cout << "Введите девятизначное число: ";
	cin >> num1;
	//      999 999 999
	// переменная = 1 цифра
	num9 = num1%10;
	num8 = (num1 %100)/10;
	num7 = (num1 % 1000) / 100;
	num6 = (num1 % 10000) / 1000;
	num5 = (num1 % 100000) / 10000;
	num4 = (num1 % 1000000) / 100000;
	num3 = (num1 % 10000000) / 1000000;
	num2 = (num1 % 100000000) / 10000000;
	num1 = (num1 % 1000000000) / 100000000;

	// 1 ищем сумму
	cout << "Ответ:\nСумма цифр: " << num2+num3+num4+num5+num6+num7+num8+num9 + num1;
	// 2 ищем произведение
	cout << "\nПроизведение цифр: " << num2 * num3 * num4 * num5 * num6 * num7 * num8 * num9 * num1;
	// 3 перевёртыш
	cout << "\nПеревёртыш: " << num9<< num8<< num7<< num6<< num5<< num4<< num3<< num2<< num1;
	// 4 сумма, но разность короче да
	cout << "\nЗнакочередующая сумма: " << num1 - num2 + num3 - num4 + num5 - num6 + num7 - num8 + num9 ;
	// 5 13579
	cout << "\nНечётная номерация цифр: " << num1<< num3<< num5<< num7<< num9;
	// 6 полиндром
	num1 = (num1 - num9) * (num1 - num9);
	num2 = (num2 - num8) * (num2 - num8);
	num3 = (num3 - num7) * (num3 - num7);
	num4 = (num4 - num6) * (num4 - num6);
	num1 = num1+num2+num3+num4;
	cout << "\nПолиндром: " << !num1;
	return 0;
}

int main() {
	setlocale(LC_ALL, "RU");
	cout << "\n\nЗадание 1:\n\n";
	quest1();
	cout << "\n\nЗадание 2:\n\n";
	quest2();
	cout << "\n\nЗадание 3:\n\n";
	quest3();
	cout << "\n\nЗадание 4:\n\n";
	quest4();
	cout << "\n\nЗадание 5:\n\n";
	quest5();
	cout << "\n\nЗадание 6:\n\n";
	quest6();
	cout << "\n\nЗадание 7:\n\n";
	quest7();
	cout << "\n\nЗадание 8:\n\n";
	quest8();
	cout << "\n\nЗадание 9:\n\n";
	quest9();
	cout << "\n\nЗадание 10:\n\n";
	quest10();
	cout << "\n\nЗадание 11:\n\n";
	quest11();
	return 0;
}