#pragma once
#include "socket_connexion_python.h"
#define	DEPTH	5
#define BADMOVE	"BADMOVE"
#define LOST	"LO"
#define WIN		"WI"
#define BLACKWIN	"BW"
#define WHITEWIN	"WW"

bool playingAgainstAi(SocketConnexion & conn);
bool AIvsAI(SocketConnexion& conn);