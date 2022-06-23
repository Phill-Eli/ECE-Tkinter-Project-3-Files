for m in missiles:
            if m.is_active() == False:
                missiles.pop(missiles.index(m))