from datetime import date
from battery.nubbin_battery import NubbinBattery
from battery.spindler_battery import SpindlerBattery
from car import Car
from engine.capulet_engine import CapuletEngine
from engine.sternman_engine import SternmanEngine
from engine.willoughby_engine import WilloughbyEngine
from tire.carrigan_tire import CarriganTire
from tire.octoprime_tire import OctoprimeTire



class CarFactory:
    
    @staticmethod
    def create_calliope(current_date:date, last_service_date: date, current_mileage: int, last_service_mileage: int, tire_wear_values = [0.0, 0.0, 0.0, 0.0]) -> Car:
        engine = CapuletEngine(current_mileage, last_service_mileage)
        battery = SpindlerBattery(last_service_date, current_date)
        tire = CarriganTire(tire_wear_values)
        return Car(engine, battery, tire)
    
    @staticmethod
    def create_glissade(current_date:date, last_service_date: date, current_mileage: int, last_service_mileage: int, tire_wear_values = [0.0, 0.0, 0.0, 0.0]) -> Car:
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        battery = SpindlerBattery(last_service_date, current_date)
        tire = CarriganTire(tire_wear_values)
        return Car(engine, battery, tire)

    @staticmethod    
    def create_palindrome(current_date: date, last_service_date: date, warning_light_on: bool, tire_wear_values = [0.0, 0.0, 0.0, 0.0]) -> Car:
        engine = SternmanEngine(warning_light_on)
        battery = SpindlerBattery(last_service_date, current_date)
        tire = OctoprimeTire(tire_wear_values)
        return Car(engine, battery, tire)

    @staticmethod
    def create_rorschach(current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int, tire_wear_values = [0.0, 0.0, 0.0, 0.0]) -> Car:
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        battery = NubbinBattery(last_service_date, current_date)
        tire = OctoprimeTire(tire_wear_values)
        return Car(engine, battery, tire)

    @staticmethod
    def create_thovex(current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int, tire_wear_values = [0.0, 0.0, 0.0, 0.0]) -> Car:
        engine = CapuletEngine(current_mileage,last_service_mileage)
        battery = NubbinBattery(last_service_date,current_date)
        tire = OctoprimeTire(tire_wear_values)
        return Car(engine, battery, tire)