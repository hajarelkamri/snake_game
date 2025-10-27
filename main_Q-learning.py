from env import Environment
from agent_brain import QLearningTable


def update():
    steps = []

    all_costs = []

    for episode in range(10000000):
        observation = env.reset()

        i = 0

        cost = 0

        while True:
            env.render()

            action = RL.choose_action(str(observation))
            observation_, reward, done = env.step(action)
            cost += RL.learn(str(observation), action, reward, str(observation_))
            observation = observation_
            i += 1

            if done:
                steps += [i]
                all_costs += [cost]
                break

    env.final()

    RL.print_q_table()
    RL.plot_results(steps, all_costs)


if __name__ == "__main__":
    env = Environment()
    RL = QLearningTable(actions=list(range(env.n_actions)))
    env.after(100, update)
    env.mainloop()