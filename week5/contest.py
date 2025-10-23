class Contest:
    def __init__(self, names, task_count):
      self.names = list(names)
      self.task_count = task_count

      self.best = {name: [0] * (task_count + 1) for name in self.names}
      self.total = {name: 0 for name in self.names}
      self.time_reached = {name: None for name in self.names}

      self._t = 0

    def add_submission(self, name, task, score):
      self._t += 1
      prev_best = self.best[name][task]
      if score > prev_best:
        new_score = score - prev_best
        self.best[name][task] = score
        self.total[name] += new_score

        self.time_reached[name] = self._t

    def create_scoreboard(self):
      rows = []
      for name in self.names:
        tot = self.total.get(name, 0)
        t = self.time_reached.get(name)

        if tot == 0:
            sort_key = (-tot, 1, name)
        else:
            sort_key = (-tot, 0, t if t is not None else float('inf'))

        rows.append((sort_key, name, tot))

      rows.sort()
      return [(name, tot) for _, name, tot in rows]


if __name__ == "__main__":
    names = ["anna", "pekka", "kalle", "tiina", "eeva"]
    contest = Contest(names, 3)

    contest.add_submission("tiina", 2, 30)
    contest.add_submission("pekka", 1, 40)
    contest.add_submission("tiina", 1, 20)
    contest.add_submission("pekka", 1, 50)
    contest.add_submission("pekka", 2, 0)
    contest.add_submission("eeva", 3, 100)
    contest.add_submission("anna", 1, 0)
    contest.add_submission("eeva", 3, 80)
    contest.add_submission("tiina", 2, 30)

    scoreboard = contest.create_scoreboard()
    print(scoreboard)
    # [('eeva', 100), ('tiina', 50), ('pekka', 50), ('anna', 0), ('kalle', 0)