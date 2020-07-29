from models import Car
cars = ['VW', 'BMW', 'OPEL']
CAR_IMAGE = '../../car.jpeg'



for car in cars:
    car_file = open(CAR_IMAGE, 'rb')
    car_obj = Car.objects.create(title = car)
    car_obj.photo.put(car_file, content_type='image/jpeg')
    car_obj.save()
    car_file.close()


