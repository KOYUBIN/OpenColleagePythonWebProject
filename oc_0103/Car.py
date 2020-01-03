class Car:
    def __init__(self, 제조사, 모델, 색상):
        self.제조사 = 제조사
        self.모델 = 모델
        self.색상 = 색상
        self.fuel = 1000

    def forward(self):
        self.fuel = self.fuel - 50
        print(self.제조사, self.모델, self.색상, "차량이 전진 중입니다! 현재 기름양은", self.fuel, "입니다.")

    def reverse(self):
        self.fuel = self.fuel - 30
        print(self.제조사, self.모델, self.색상, "차량이 후진 중입니다! 현재 기름양은", self.fuel, "입니다.")


class ElectricCar(Car):
    def __init__(self, 제조사, 모델, 색상):
        super().__init__(self, 제조사, 모델, 색상)
        self.충전잔량 = 100

    def forward(self):
        self.충전잔량 = self.충전잔량 - 10
        print(self.제조사, self.모델, self.색상, "차량이 전진 중입니다! 현재 충전잔량은", self.충전잔량, "입니다.")

    def reverse(self):
        self.충전잔량 = self.충전잔량 - 5
        print(self.제조사, self.모델, self.색상, "차량이 후진 중입니다! 현재 충전잔량양은", self.충전잔량, "입니다.")


ElectricCar1 = ElectricCar("가", "a", "White")
ElectricCar2 = ElectricCar("나", "b", "Black")
ElectricCar3 = ElectricCar("다", "c", "Red")

ElectricCar1.forward()
ElectricCar1.reverse()
ElectricCar2.forward()
ElectricCar2.reverse()
ElectricCar3.forward()
ElectricCar3.reverse()

