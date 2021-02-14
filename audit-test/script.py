import krpc
conn = krpc.connect(name='Jyuza')
vessel = conn.space_center.active_vessel
print(vessel.name)