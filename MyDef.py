def my():

    YforBird = pipes[0].bottom + 100

    for x, bird in enumerate(birds):
        bird.move()
        ge[x].fitness += 0.1

        output = nets[x].activate((bird.y, abs(bird.y - pipes[pipe_ind].height), abs(bird.y - pipes[pipe_ind].bottom)))

        if output[0] > 0.5:
            bird.jump()



