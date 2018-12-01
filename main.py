import view as v
import model as m
import controller as c

ctrl = c.Controller(v.View(), m.Model())
ctrl.start()