# Slide Puzzle
# By Al Sweigart al@inventwithpython.com
# http://inventwithpython.com/pygame
# Released under a "Simplified BSD" license

import pygame, sys, random, Board
from pygame.locals import *

# Create the constants (go ahead and experiment with different values)


# BoardData is a class for datastructure of the board which all data is stored in it and retreved from it \\Kamel
BoardData = Board.Board(5)

WINDOWWIDTH = 740
WINDOWHEIGHT = 480
XMARGIN = int((WINDOWWIDTH - (BoardData.getTILESIZE() * BoardData.getBOARDERSIZE() + (BoardData.getBOARDERSIZE() - 1))) / 2)
YMARGIN = int((WINDOWHEIGHT - (BoardData.getTILESIZE() * BoardData.getBOARDERSIZE() + (BoardData.getBOARDERSIZE() - 1))) / 2)
FPS = 30
BLANK = None

#                 R    G    B
BLACK =         (  0,   0,   0)
WHITE =         (255, 255, 255)
BRIGHTBLUE =    (  0,  50, 255)
DARKTURQUOISE = (  3,  54,  73)
GREEN =         (  0, 204,   0)

BGCOLOR = DARKTURQUOISE
TILECOLOR = GREEN
TEXTCOLOR = WHITE
BORDERCOLOR = BRIGHTBLUE
BASICFONTSIZE = 20

BUTTONCOLOR = WHITE
BUTTONTEXTCOLOR = BLACK
MESSAGECOLOR = WHITE

UP = 'up'
DOWN = 'down'
LEFT = 'left'
RIGHT = 'right'

def main():
    global FPSCLOCK, DISPLAYSURF, BASICFONT, RESET_SURF, RESET_RECT, NEW_SURF, NEW_RECT, SOLVE_SURF, SOLVE_RECT, S3_SURF, S3_RECT, S4_SURF, S4_RECT, S5_SURF, S5_RECT, H1_SURF, H1_RECT, H2_SURF, H2_RECT, H3_SURF, H3_RECT, H4_SURF, H4_RECT, H5_SURF, H5_RECT, counterTextSURF, counterTextRECT, counterSURF, counterRECT, test

    test = True  # variable to check wither the puzzle size is chosen or not to disaple updating it while working
    msg = 'Choose "Puzzle size" then choose "Heuristic" then press SOLVE'
    pygame.init()
    FPSCLOCK = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
    pygame.display.set_caption('N-Puzzle')
    BASICFONT = pygame.font.Font('freesansbold.ttf', BASICFONTSIZE)

    # Store the option buttons and their rectangles in OPTIONS.
    RESET_SURF, RESET_RECT = makeText('Reset',    TEXTCOLOR, TILECOLOR, WINDOWWIDTH - 120, WINDOWHEIGHT - 90)
    NEW_SURF,   NEW_RECT   = makeText('New Game', TEXTCOLOR, TILECOLOR, WINDOWWIDTH - 120, WINDOWHEIGHT - 60)
    SOLVE_SURF, SOLVE_RECT = makeText('Solve',    TEXTCOLOR, TILECOLOR, WINDOWWIDTH - 120, WINDOWHEIGHT - 30)
    S3_SURF, S3_RECT = makeText('8-Puzzle', TEXTCOLOR, TILECOLOR, WINDOWWIDTH - 700, WINDOWHEIGHT - 300)
    S4_SURF, S4_RECT = makeText('16-Puzzle', TEXTCOLOR, TILECOLOR, WINDOWWIDTH - 700, WINDOWHEIGHT - 260)
    S5_SURF, S5_RECT = makeText('24-Puzzle', TEXTCOLOR, TILECOLOR, WINDOWWIDTH - 700, WINDOWHEIGHT - 220)
    H1_SURF, H1_RECT = makeText('Heurestic 1', TEXTCOLOR, TILECOLOR, WINDOWWIDTH - 120, WINDOWHEIGHT - 430)
    H2_SURF, H2_RECT = makeText('Heurestic 2', TEXTCOLOR, TILECOLOR, WINDOWWIDTH - 120, WINDOWHEIGHT - 400)
    H3_SURF, H3_RECT = makeText('Heurestic 3', TEXTCOLOR, TILECOLOR, WINDOWWIDTH - 120, WINDOWHEIGHT - 370)
    H4_SURF, H4_RECT = makeText('Heurestic 4', TEXTCOLOR, TILECOLOR, WINDOWWIDTH - 120, WINDOWHEIGHT - 340)
    H5_SURF, H5_RECT = makeText('Heurestic 5', TEXTCOLOR, TILECOLOR, WINDOWWIDTH - 120, WINDOWHEIGHT - 310)
    counterTextSURF, counterTextRECT = makeText("Number of Moves", MESSAGECOLOR, BGCOLOR, 5, 30)
    counterSURF, counterRECT = makeText(str(BoardData.getMovCounter()), MESSAGECOLOR, BGCOLOR, 190,30)

    mainBoard = BoardData.getBoard()
    drawBoard(mainBoard, msg)  #Draw starting board as goal board

    SOLVEDBOARD = BoardData.getBoard() # a solved board is the same as the board in a start state.

    allMoves = [] # list of moves made from the solved configuration

    while True: # main game loop
        slideTo = None # the direction, if any, a tile should slide
        if mainBoard == SOLVEDBOARD and not test:
            msg = 'Solved!'

        checkForQuit()
        for event in pygame.event.get(): # event handling loop
            if event.type == MOUSEBUTTONUP:
                spotx, spoty = getSpotClicked(mainBoard, event.pos[0], event.pos[1])

                if (spotx, spoty) == (None, None):
                    # check if the user clicked on an option button
                    #Determine which button was clicked \\Kamel
                    if S3_RECT.collidepoint(event.pos) and test:
                        BoardData.setBOARDERSIZE(3)
                        BoardData.resetMovCounter()
                        mainBoard = BoardData.getBoard()
                        drawBoard(mainBoard, msg)
                    elif S4_RECT.collidepoint(event.pos) and test:
                        BoardData.setBOARDERSIZE(4)
                        BoardData.resetMovCounter()
                        mainBoard = BoardData.getBoard()
                        drawBoard(mainBoard, msg)
                    elif S5_RECT.collidepoint(event.pos) and test:
                        BoardData.setBOARDERSIZE(5)
                        BoardData.resetMovCounter()
                        mainBoard = BoardData.getBoard()
                        drawBoard(mainBoard, msg)
                    #Choosing the heuristic \\Kamel
                    elif H1_RECT.collidepoint(event.pos):
                        return None
                    elif H2_RECT.collidepoint(event.pos):
                        return None
                    elif H3_RECT.collidepoint(event.pos):
                        return None
                    elif H4_RECT.collidepoint(event.pos):
                        return None
                    elif H5_RECT.collidepoint(event.pos):
                        return None
                    elif RESET_RECT.collidepoint(event.pos):
                        resetAnimation(mainBoard, allMoves) # clicked on Reset button
                        allMoves = []
                        test = True
                    elif NEW_RECT.collidepoint(event.pos):
                        mainBoard = generateNewPuzzle(random.randint(10, 100)) # clicked on New Game button
                        test = True
                    elif SOLVE_RECT.collidepoint(event.pos):
                        drawBoard(mainBoard, None)
                        test = False


                else:
                    # check if the clicked tile was next to the blank spot

                    blankx, blanky = getBlankPosition(mainBoard)
                    if spotx == blankx + 1 and spoty == blanky:
                        slideTo = LEFT
                    elif spotx == blankx - 1 and spoty == blanky:
                        slideTo = RIGHT
                    elif spotx == blankx and spoty == blanky + 1:
                        slideTo = UP
                    elif spotx == blankx and spoty == blanky - 1:
                        slideTo = DOWN

            elif event.type == KEYUP:
                # check if the user pressed a key to slide a tile
                if event.key in (K_LEFT, K_a) and isValidMove(mainBoard, LEFT):
                    slideTo = LEFT
                elif event.key in (K_RIGHT, K_d) and isValidMove(mainBoard, RIGHT):
                    slideTo = RIGHT
                elif event.key in (K_UP, K_w) and isValidMove(mainBoard, UP):
                    slideTo = UP
                elif event.key in (K_DOWN, K_s) and isValidMove(mainBoard, DOWN):
                    slideTo = DOWN

        if slideTo:
            slideAnimation(mainBoard, slideTo, 'Click tile or press arrow keys to slide.', 8) # show slide on screen
            makeMove(mainBoard, slideTo)
            allMoves.append(slideTo) # record the slide
        pygame.display.update()
        FPSCLOCK.tick(FPS)


def terminate():
    pygame.quit()
    sys.exit()


def checkForQuit():
    for event in pygame.event.get(QUIT): # get all the QUIT events
        terminate() # terminate if any QUIT events are present
    for event in pygame.event.get(KEYUP): # get all the KEYUP events
        if event.key == K_ESCAPE:
            terminate() # terminate if the KEYUP event was for the Esc key
        pygame.event.post(event) # put the other KEYUP event objects back


def getBlankPosition(board):
    # Return the x and y of board coordinates of the blank space.
    for x in range(len(board)):
        for y in range(len(board)):
            if board[x][y] == BLANK:
                return (x, y)


def makeMove(board, move):
    # This function does not check if the move is valid.
    blankx, blanky = getBlankPosition(board)

    if move == UP and isValidMove(board, move):
        board[blankx][blanky], board[blankx][blanky + 1] = board[blankx][blanky + 1], board[blankx][blanky]
        BoardData.incMovCounter()
    elif move == DOWN and isValidMove(board, move):
        board[blankx][blanky], board[blankx][blanky - 1] = board[blankx][blanky - 1], board[blankx][blanky]
        BoardData.incMovCounter()
    elif move == LEFT and isValidMove(board, move):
        board[blankx][blanky], board[blankx + 1][blanky] = board[blankx + 1][blanky], board[blankx][blanky]
        BoardData.incMovCounter()
    elif move == RIGHT and isValidMove(board, move):
        board[blankx][blanky], board[blankx - 1][blanky] = board[blankx - 1][blanky], board[blankx][blanky]
        BoardData.incMovCounter()


def isValidMove(board, move):
    blankx, blanky = getBlankPosition(board)
    return (move == UP and blanky != len(board[0]) - 1) or \
           (move == DOWN and blanky != 0) or \
           (move == LEFT and blankx != len(board) - 1) or \
           (move == RIGHT and blankx != 0)


def getRandomMove(board, lastMove=None):
    # start with a full list of all four moves
    validMoves = [UP, DOWN, LEFT, RIGHT]

    # remove moves from the list as they are disqualified
    if lastMove == UP or not isValidMove(board, DOWN):
        validMoves.remove(DOWN)
    if lastMove == DOWN or not isValidMove(board, UP):
        validMoves.remove(UP)
    if lastMove == LEFT or not isValidMove(board, RIGHT):
        validMoves.remove(RIGHT)
    if lastMove == RIGHT or not isValidMove(board, LEFT):
        validMoves.remove(LEFT)

    # return a random move from the list of remaining moves
    return random.choice(validMoves)


def getLeftTopOfTile(tileX, tileY):
    left = XMARGIN + (tileX * BoardData.getTILESIZE()) + (tileX - 1)
    top = YMARGIN + (tileY * BoardData.getTILESIZE()) + (tileY - 1)
    return (left, top)


def getSpotClicked(board, x, y):
    # from the x & y pixel coordinates, get the x & y board coordinates
    for tileX in range(len(board)):
        for tileY in range(len(board[0])):
            left, top = getLeftTopOfTile(tileX, tileY)
            tileRect = pygame.Rect(left, top, BoardData.getTILESIZE(), BoardData.getTILESIZE())
            if tileRect.collidepoint(x, y):
                return (tileX, tileY)
    return (None, None)


def drawTile(tilex, tiley, number, adjx=0, adjy=0):
    # draw a tile at board coordinates tilex and tiley, optionally a few
    # pixels over (determined by adjx and adjy)
    left, top = getLeftTopOfTile(tilex, tiley)
    pygame.draw.rect(DISPLAYSURF, TILECOLOR, (left + adjx, top + adjy, BoardData.getTILESIZE(), BoardData.getTILESIZE()))
    textSurf = BASICFONT.render(str(number), True, TEXTCOLOR)
    textRect = textSurf.get_rect()
    textRect.center = left + int(BoardData.getTILESIZE() / 2) + adjx, top + int(BoardData.getTILESIZE() / 2) + adjy
    DISPLAYSURF.blit(textSurf, textRect)


def makeText(text, color, bgcolor, top, left):
    # create the Surface and Rect objects for some text.
    textSurf = BASICFONT.render(text, True, color, bgcolor)
    textRect = textSurf.get_rect()
    textRect.topleft = (top, left)
    return (textSurf, textRect)


def drawBoard(board, message):
    DISPLAYSURF.fill(BGCOLOR)
    if message:
        textSurf, textRect = makeText(message, MESSAGECOLOR, BGCOLOR, 5, 5)
        DISPLAYSURF.blit(textSurf, textRect)

    for tilex in range(len(board)):
        for tiley in range(len(board[0])):
            if board[tilex][tiley]:
                drawTile(tilex, tiley, board[tilex][tiley])

#Draw the board border (Blue line around the tiles) \\Kamel
    left, top = getLeftTopOfTile(0, 0)
    width = 250
    height = 250
    pygame.draw.rect(DISPLAYSURF, BORDERCOLOR, (left - 5, top - 5, width + 11, height + 11), 4)

    DISPLAYSURF.blit(RESET_SURF, RESET_RECT)
    DISPLAYSURF.blit(NEW_SURF, NEW_RECT)
    DISPLAYSURF.blit(SOLVE_SURF, SOLVE_RECT)
    DISPLAYSURF.blit(S3_SURF, S3_RECT)
    DISPLAYSURF.blit(S4_SURF, S4_RECT)
    DISPLAYSURF.blit(S5_SURF, S5_RECT)
    DISPLAYSURF.blit(H1_SURF, H1_RECT)
    DISPLAYSURF.blit(H2_SURF, H2_RECT)
    DISPLAYSURF.blit(H3_SURF, H3_RECT)
    DISPLAYSURF.blit(H4_SURF, H4_RECT)
    DISPLAYSURF.blit(H5_SURF, H5_RECT)
    DISPLAYSURF.blit(counterTextSURF, counterTextRECT)
    counterSURF, counterRECT = makeText(str(BoardData.getMovCounter()), MESSAGECOLOR, BGCOLOR, 190,30)
    DISPLAYSURF.blit(counterSURF, counterRECT)


def slideAnimation(board, direction, message, animationSpeed):
    # Note: This function does not check if the move is valid.

    blankx, blanky = getBlankPosition(board)
    if direction == UP:
        movex = blankx
        movey = blanky + 1
    elif direction == DOWN:
        movex = blankx
        movey = blanky - 1
    elif direction == LEFT:
        movex = blankx + 1
        movey = blanky
    elif direction == RIGHT:
        movex = blankx - 1
        movey = blanky

    # prepare the base surface
    drawBoard(board, message)
    baseSurf = DISPLAYSURF.copy()
    # draw a blank space over the moving tile on the baseSurf Surface.
    moveLeft, moveTop = getLeftTopOfTile(movex, movey)
    pygame.draw.rect(baseSurf, BGCOLOR, (moveLeft, moveTop, BoardData.getTILESIZE(), BoardData.getTILESIZE()))

    for i in range(0, BoardData.getTILESIZE(), animationSpeed):
        # animate the tile sliding over
        checkForQuit()
        DISPLAYSURF.blit(baseSurf, (0, 0))
        if direction == UP:
            drawTile(movex, movey, board[movex][movey], 0, -i)
        if direction == DOWN:
            drawTile(movex, movey, board[movex][movey], 0, i)
        if direction == LEFT:
            drawTile(movex, movey, board[movex][movey], -i, 0)
        if direction == RIGHT:
            drawTile(movex, movey, board[movex][movey], i, 0)

        pygame.display.update()
        DISPLAYSURF.blit(counterTextSURF, counterTextRECT)
        counterSURF, counterRECT = makeText(str(BoardData.getMovCounter()), MESSAGECOLOR, BGCOLOR, 190,30)
        DISPLAYSURF.blit(counterSURF, counterRECT)
        FPSCLOCK.tick(FPS)


def generateNewPuzzle(numSlides):
    # From a starting configuration, make numSlides number of moves (and
    # animate these moves).
    board = BoardData.getBoard()
    drawBoard(board, '')
    pygame.display.update()
    pygame.time.wait(500) # pause 500 milliseconds for effect
    lastMove = None
    for i in range(numSlides):
        move = getRandomMove(board, lastMove)
        slideAnimation(board, move, 'Generating new puzzle...', animationSpeed=int(BoardData.getTILESIZE() / 3))
        makeMove(board, move)
        BoardData.resetMovCounter()
        lastMove = move
    return board


def resetAnimation(board, allMoves):
    # make all of the moves in allMoves in reverse.
    revAllMoves = allMoves[:] # gets a copy of the list
    revAllMoves.reverse()

    for move in revAllMoves:
        if move == UP:
            oppositeMove = DOWN
        elif move == DOWN:
            oppositeMove = UP
        elif move == RIGHT:
            oppositeMove = LEFT
        elif move == LEFT:
            oppositeMove = RIGHT
        slideAnimation(board, oppositeMove, '', animationSpeed=int(BoardData.getTILESIZE() / 2))
        BoardData.resetMovCounter()
        makeMove(board, oppositeMove)


if __name__ == '__main__':
    main()