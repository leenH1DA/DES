import random

from DES import des, time_units

cars0 = des.DES() \
    .set_sample_size(12) \
    .set_seed(42) \
    .set_time_between_distro(random.uniform, a=1, b=7) \
    .set_service_time_distro(random.uniform, a=1, b=4) \
    .set_entity_name("Car") \
    .set_time_unit(time_units.TimeUnit.Min)

cars1 = des.DES() \
    .set_sample_size(12) \
    .set_seed(42) \
    .set_time_between_distro(random.uniform, a=1, b=7) \
    .set_service_time_distro(random.expovariate, lambd=.5) \
    .set_entity_name("Car") \
    .set_time_unit(time_units.TimeUnit.Min)

cars0.run()
cars1.run()
print(cars0.df["wait_time"].mean())
print(cars1.df["wait_time"].mean())
