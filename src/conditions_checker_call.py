def conditions_checker_call(gs, moves_left, check, repeat_check, checkmate, moves_draw, check_only_king_left):

    checkmate(gs, moves_left, check)

    repeat_check(gs)

    check_only_king_left(gs)

    moves_draw(gs)
