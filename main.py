from env import Environment
from agent_brain import SarsaTable


def update():
    steps = []

    all_costs = []

    for episode in range(6000):
        observation = env.reset()

        i = 0

        cost = 0

        action = RL.choose_action(str(observation))

        while True:
            env.render()
            observation_, reward, done = env.step(action)
            action_ = RL.choose_action(str(observation_))
            cost += RL.learn(str(observation), action, reward, str(observation_), action_)
            observation = observation_
            action = action_
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
    RL = SarsaTable(actions=list(range(env.n_actions)),
                    learning_rate=1,
                    reward_decay=0.9,
                    e_greedy=0.9)
    env.after(100, update)
    env.mainloop()