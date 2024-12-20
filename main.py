import random
from DES import des, time_units


cars1 = des.DES() \
    .set_sample_size(12) \
    .set_seed(42) \
    .set_time_between_distro(random.uniform, a=1, b=7) \
    .set_service_time_distro(random.uniform, a=1, b=4) \
    .set_system_name("TollBooth") \
    .set_entity_name("Car") \
    .set_time_unit(time_units.TimeUnit.Min)

for car in des.run_simulations(cars1, 10):
    car.run()
    car.plot()
    car.save_to("csv")
