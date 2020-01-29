#include "playingModes.h"
#include <iostream>
#include "board.h"
#include "ai.h"

using namespace std;

bool playingAgainstAi(SocketConnexion & conn)
{
	// Special variables
	char bad_move[] = BADMOVE;
	char lost[] = LOST;
	char win[] = WIN;
	const short depth = DEPTH;

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

			if (player_move[0] == 'M' and player_move[1] == 'E') {
				cout << "[*] Going to menu." << endl;
				return false;
			}

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
		string reply = transform_chessboard_to_move(before, b, BLACK);

		if (b.get_bitboard_children_cpp().size() == 0) {
			cout << "[--] Vous avez perdu !" << endl;
			reply += "#LO";
		}
		cout << "[*] Sending computer move " << reply << " to player." << endl;
		conn.send_string(reply);
	}

	b.print();

	return true;
}

bool AIvsAI(SocketConnexion & conn)
{
	const short depth = DEPTH;	
	char blackwin[] = BLACKWIN;
	char whitewin[] = WHITEWIN;

	cout << "[+] Creating board." << endl;
	Board b = Board();

	// Playing
	cout << "[+] Begining to play." << endl;
	bool haswon = false;
	bool player = true;  // true for White, false for Black

	while (!haswon && b.get_bitboard_children_cpp().size() != 0) {
		b.print();

		const Board before = b;
		b = select_best_move(b, depth, player, haswon);

		if (haswon) {
			cout << "[+] Echec et mat." << endl;
			conn.send_data(player ? whitewin : blackwin);
			break;
		}
		string reply = transform_chessboard_to_move(before, b, player ? WHITE : BLACK);

		// waiting for move done
		string ready = "  ";
		while (!(ready[0] == 'R' && ready[1] == 'E'))
			ready = conn.recv_data();

		cout << "[*] Sending computer move " << reply << " to player." << endl;
		conn.send_string(reply);

		player = !player;
	}

	b.print();

	return false;
}
