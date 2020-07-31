
def simulation(
    termination_criteria,
    particles,
    particle_neighborhood,
    fitness_function,
    velocity_update,
    update_best

):
    while not termination_criteria():
        for particle in particles:
            # update velocity, update position, update personal_best
            particle.fly(
                particle_neighborhood(particles),
                velocity_update,
                fitness_function)
            update_best(particle, fitness_function)
