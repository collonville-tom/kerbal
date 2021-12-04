import krpc
import sys
import logging as log


def init_logger():
    log.basicConfig(filename='auditRun.log', level=log.DEBUG, format='%(asctime)s-%(levelname)s-%(message)s')
    log.info("INIT RUN")
    log.info("INIT RUN")
    log.info("INIT RUN")

def get_game_connexion():
    log.info("Etablissement de la connexion au jeux")
    game_connexion = krpc.connect(name='CommandModule')
    log.info("Etablissement de la connexion au jeux realisé")
    return game_connexion


def main() -> int:
    init_logger()
    log.info("Launching CommandModule")
    game_connexion=get_game_connexion()
    space_center= game_connexion.space_center
    #vessel_to_launch=space_center.launchable_vesels("VAB")
    ##log.info("Launching {}", vessel_to_launch[0])
    #vx=space_center.vessels[0]
    #space_center.launch_vessel_from_vab(vessel_to_launch[0],True)
    
    vx=space_center.active_vessel
    log.info(vx.flight().horizontal_speed)
    vx.control.activate_next_stage()


    return 0



if __name__ == '__main__':
    sys.exit(main())