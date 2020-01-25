// chess_engine.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

#include <iostream>
#include <fstream>
#include <string>
#include <cstring>
#include <csignal>
#include "socket_connexion_python.h"

#include "ai.h"
#include "saving.h"

void shutdownServer(int signum);

using namespace std;

int main()
{	
	// Special variables
	char bad_move[] = "BADMOVE";
	char lost[] = "LO";
	char win[] = "WI";
	const short depth = 5;
	// register signal SIGINT and signal handler  
	signal(SIGINT, shutdownServer);

	while (true) {
		// Establishing connection
		cout << "[+] Opening port " << PORT << "." << endl;
		bool error = false;
		SocketConnexion conn = SocketConnexion(error);
		if (error) {
			cout << "[-] There was a problem establishing the connection, leaving..." << endl;
			return 1;
		}

		while (true) {
			cout << "[+] Creating board." << endl;
			Board b = Board();


			// Playing
			cout << "[+] Begining to play." << endl;
			bool haswon = false;
			while (!haswon && b.get_bitboard_children_cpp().size() != 0) {
				b.print();

				bool legal_move = false;
				while (!legal_move) {

					// Receiving player move
					string player_move = string(conn.recv_data());
					cout << "[*] Receiving player move : " << player_move << "." << endl;

					// Apply player move
					legal_move = move_piece(b, player_move);
					if (!legal_move)
						conn.send_data(bad_move);
				}

				const Board before = b;
				b = select_best_move(b, depth, false, haswon);
				if (haswon) {
					cout << "[++] WOW ! Vous avez gagné !" << endl;
					conn.send_data(win);
					break;
				}
				string reply = transform_chessboard_to_move_BLACK(before, b);

				if (b.get_bitboard_children_cpp().size() == 0) {
					cout << "[--] Vous avez perdu !" << endl;
					reply += "#LO";
				}
				cout << "[*] Sending computer move " << reply << " to player." << endl;
				conn.send_string(reply);
			}

			b.print();

			// next action
			string action = string(conn.recv_data());
			if (action == "EN")
				break;
			else if (action == "ST")
				continue;
		}
		cout << "[*] Reopening port in a moment for maybe a new connection later." << endl;
		Sleep(2000);  // wait 2 seconds before reopening the server
	}
	return 0;
}

void shutdownServer(int signum) {
	cout << "[*] Shutdown" << endl;
}