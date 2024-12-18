import random

from DES.des import DES, run_simulations
from DES.time_units import TimeUnit

cars = DES() \
    .set_sample_size(12) \
    .set_seed(42) \
    .set_time_between_distro(random.uniform, a=1, b=7) \
    .set_service_time_distro(random.uniform, a=1, b=4) \
    .set_entity_name("Car") \
    .set_time_unit(TimeUnit.Min)

cars.run()

for sim in run_simulations(cars, 10):
    sim.run()
    sim.save_to()