from randvis.simulation import DVSim

# Should add fixture to remove generated image and movie files.


def test_sim():
    sim = DVSim((3, 5), 0.1, 12345, '.')
    sim.simulate(5, 1, 5)
    sim.make_movie()
