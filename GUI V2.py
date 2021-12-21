# Slide Puzzle
# By Al Sweigart al@inventwithpython.com
# http://inventwithpython.com/pygame
# Released under a "Simplified BSD" license

import pygame, sys, random
from pygame.locals import *
from copy import deepcopy
from operator import itemgetter
from Heuristic import Heuristic
from Board import Board


class GUI:
    # Create the constants (go ahead and experiment with different values)
    # BoardData is a class for datastructure of the board which all data is stored in it and retreved from it \\Kamel

    BoardData = Board(3)

    def __init__(self):
        self.solution = list()
        self.Space = {}
        self.Fronte = list()
        self.key = 0
        self.Goal = self.BoardData.getBoard()
        self.CloseList = list()
        self.allMoves = list()  

    WINDOWWIDTH = 740
    WINDOWHEIGHT = 480
    XMARGIN = int(
        (WINDOWWIDTH - (BoardData.getTILESIZE() * BoardData.getBOARDERSIZE() + (BoardData.getBOARDERSIZE() - 1))) / 2)
    YMARGIN = int(
        (WINDOWHEIGHT - (BoardData.getTILESIZE() * BoardData.getBOARDERSIZE() + (BoardData.getBOARDERSIZE() - 1))) / 2)
    FPS = 30
    BLANK = None

    #                 R    G    B
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    BRIGHTBLUE = (0, 50, 255)
    DARKTURQUOISE = (3, 54, 73)
    GREEN = (0, 204, 0)

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

    def main(self):
        global FPSCLOCK, DISPLAYSURF, BASICFONT, RESET_SURF, RESET_RECT, NEW_SURF, NEW_RECT, SOLVE_SURF, SOLVE_RECT, S3_SURF, S3_RECT, S4_SURF, S4_RECT, S5_SURF, S5_RECT, H1_SURF, H1_RECT, Euclidean_SURF, Euclidean_RECT, H3_SURF, H3_RECT, H4_SURF, H4_RECT, H5_SURF, H5_RECT, counterTextSURF, counterTextRECT, counterSURF, counterRECT, resizeable

        resizeable = True  # variable to check wither the puzzle size is chosen or not to disaple updating it while working
        msg = 'Choose "Puzzle size" then choose "Heuristic" then press SOLVE'
        pygame.init()
        FPSCLOCK = pygame.time.Clock()
        DISPLAYSURF = pygame.display.set_mode((self.WINDOWWIDTH, self.WINDOWHEIGHT))
        pygame.display.set_caption('N-Puzzle')
        BASICFONT = pygame.font.Font('freesansbold.ttf', self.BASICFONTSIZE)

        # Store the option buttons and their rectangles in OPTIONS.
        RESET_SURF, RESET_RECT = self.makeText('Reset', self.TEXTCOLOR, self.TILECOLOR, self.WINDOWWIDTH - 120, self.WINDOWHEIGHT - 90)
        NEW_SURF, NEW_RECT = self.makeText('New Game', self.TEXTCOLOR, self.TILECOLOR, self.WINDOWWIDTH - 120, self.WINDOWHEIGHT - 60)
        SOLVE_SURF, SOLVE_RECT = self.makeText('Solve', self.TEXTCOLOR, self.TILECOLOR, self.WINDOWWIDTH - 120, self.WINDOWHEIGHT - 30)
        S3_SURF, S3_RECT = self.makeText('8-Puzzle', self.TEXTCOLOR, self.TILECOLOR, self.WINDOWWIDTH - 700, self.WINDOWHEIGHT - 300)
        S4_SURF, S4_RECT = self.makeText('16-Puzzle', self.TEXTCOLOR, self.TILECOLOR, self.WINDOWWIDTH - 700, self.WINDOWHEIGHT - 260)
        S5_SURF, S5_RECT = self.makeText('24-Puzzle', self.TEXTCOLOR, self.TILECOLOR, self.WINDOWWIDTH - 700, self.WINDOWHEIGHT - 220)
        H1_SURF, H1_RECT = self.makeText('Heurestic 1', self.TEXTCOLOR, self.TILECOLOR, self.WINDOWWIDTH - 120, self.WINDOWHEIGHT - 430)
        Euclidean_SURF, Euclidean_RECT = self.makeText('Euclidean', self.TEXTCOLOR, self.TILECOLOR, self.WINDOWWIDTH - 120, self.WINDOWHEIGHT - 400)
        H3_SURF, H3_RECT = self.makeText('Heurestic 3', self.TEXTCOLOR, self.TILECOLOR, self.WINDOWWIDTH - 120, self.WINDOWHEIGHT - 370)
        H4_SURF, H4_RECT = self.makeText('Heurestic 4', self.TEXTCOLOR, self.TILECOLOR, self.WINDOWWIDTH - 120, self.WINDOWHEIGHT - 340)
        H5_SURF, H5_RECT = self.makeText('Heurestic 5', self.TEXTCOLOR, self.TILECOLOR, self.WINDOWWIDTH - 120, self.WINDOWHEIGHT - 310)
        counterTextSURF, counterTextRECT = self.makeText("Number of Moves", self.MESSAGECOLOR, self.BGCOLOR, 5, 30)
        counterSURF, counterRECT = self.makeText(str(self.BoardData.getMovCounter()), self.MESSAGECOLOR, self.BGCOLOR, 190, 30)

        mainBoard = deepcopy(self.Goal)
        self.drawBoard(mainBoard, msg)  # Draw starting board as goal board

        SOLVEDBOARD = deepcopy(mainBoard)  # a solved board is the same as the board in a start state.


        while True:  # main game loop
            slideTo = None  # the direction, if any, a tile should slide
            if mainBoard == SOLVEDBOARD and not resizeable:
                msg = 'Solved!'

            self.checkForQuit()
            for event in pygame.event.get():  # event handling loop
                if event.type == MOUSEBUTTONUP:
                    spotx, spoty = self.getSpotClicked(event.pos[0], event.pos[1])

                    if (spotx, spoty) == (None, None):
                        # check if the user clicked on an option button
                        # Determine which button was clicked \\Kamel
                        if S3_RECT.collidepoint(event.pos) and resizeable:
                            self.BoardData = Board(3)
                            self.BoardData.resetMovCounter()
                            mainBoard = self.BoardData.getBoard()
                            self.Goal = self.BoardData.getBoard()
                            self.drawBoard(mainBoard, msg)
                        elif S4_RECT.collidepoint(event.pos) and resizeable:
                            self.BoardData = Board(4)
                            self.BoardData.resetMovCounter()
                            mainBoard = self.BoardData.getBoard()
                            self.Goal = self.BoardData.getBoard()
                            self.drawBoard(mainBoard, msg)
                        elif S5_RECT.collidepoint(event.pos) and resizeable:
                            self.BoardData = Board(5)
                            self.BoardData.resetMovCounter()
                            mainBoard = self.BoardData.getBoard()
                            self.Goal = self.BoardData.getBoard()
                            self.drawBoard(mainBoard, msg)
                        # Choosing the heuristic \\Kamel
                        elif H1_RECT.collidepoint(event.pos):
                            self.creatSearchSpace(mainBoard, Heuristic().Hamming)
                        elif Euclidean_RECT.collidepoint(event.pos):
                            print(self.Goal)
                            self.creatSearchSpace(mainBoard, Heuristic().Euclidean)
                        elif H3_RECT.collidepoint(event.pos):
                            self.creatSearchSpace(mainBoard, Heuristic().Manhattan)
                        elif H4_RECT.collidepoint(event.pos):
                            self.creatSearchSpace(mainBoard, Heuristic().linear_conflicts)
                        elif H5_RECT.collidepoint(event.pos):
                            self.creatSearchSpace(mainBoard, Heuristic().Permutation)
                        elif NEW_RECT.collidepoint(event.pos):
                            mainBoard = self.generateNewPuzzle(random.randint(10, 20))  # clicked on New Game button
                        elif SOLVE_RECT.collidepoint(event.pos):
                            resizeable = False
                            ss = self.correctsoltion(self.BoardData.getSolution())
                            self.resetAnimation(mainBoard, ss)
                            # self.drawBoard(mainBoard, "solved")
                            self.solution.clear()
                            self.Space.clear()
                            self.Fronte.clear()
                            self.key = 0
                            self.CloseList.clear()
                            resizeable = True
                        elif RESET_RECT.collidepoint(event.pos):
                            self.allMoves.reverse()
                            self.resetAnimation(mainBoard, self.allMoves) # clicked on Reset button
                            self.allMoves = list()
                    else:
                        # check if the clicked tile was next to the blank spot
                        blankx, blanky = self.getBlankPosition(mainBoard)
                        if spotx == blankx + 1 and spoty == blanky:
                            slideTo = self.LEFT
                        elif spotx == blankx - 1 and spoty == blanky:
                            slideTo = self.RIGHT
                        elif spotx == blankx and spoty == blanky + 1:
                            slideTo = self.UP
                        elif spotx == blankx and spoty == blanky - 1:
                            slideTo = self.DOWN

                elif event.type == KEYUP:
                    # check if the user pressed a key to slide a tile
                    if event.key in (K_LEFT, K_a) and self.isValidMove(mainBoard, self.LEFT):
                        slideTo = self.LEFT
                    elif event.key in (K_RIGHT, K_d) and self.isValidMove(mainBoard, self.RIGHT):
                        slideTo = self.RIGHT
                    elif event.key in (K_UP, K_w) and self.isValidMove(mainBoard, self.UP):
                        slideTo = self.UP
                    elif event.key in (K_DOWN, K_s) and self.isValidMove(mainBoard, self.DOWN):
                        slideTo = self.DOWN

            if slideTo:
                self.slideAnimation(mainBoard, slideTo, msg, 8)  # show slide on screen
                self.makeMove(mainBoard, slideTo)
                self.allMoves.append(slideTo)  # record the slide
            pygame.display.update()
            FPSCLOCK.tick(self.FPS)

    def terminate(self):
        pygame.quit()
        sys.exit()

    def checkForQuit(self):
        for event in pygame.event.get(QUIT):  # get all the QUIT events
            self.terminate()  # terminate if any QUIT events are present
        for event in pygame.event.get(KEYUP):  # get all the KEYUP events
            if event.key == K_ESCAPE:
                self.terminate()  # terminate if the KEYUP event was for the Esc key
            pygame.event.post(event)  # put the other KEYUP event objects back

    def getBlankPosition(self, board): # Return the x and y of board coordinates of the blank space.
        n = self.BoardData.getBOARDERSIZE()
        for x in range(n):
            for y in range(n):
                if board[x][y] == self.BLANK:
                    return (x, y)

    def makeMove(self, board, move):
        blankx, blanky = self.getBlankPosition(board)
        # print('*' * 50)
        # print(str(np.transpose(np.array(board))) + "\n?????????????????????\n" + str(np.array(board)))
        # print('Blank of x:' + str(blankx) + '\nBlank of y:' + str(blanky))
        # print('*' * 50)
        if move == self.UP and self.isValidMove(board, move):
            board[blankx][blanky], board[blankx][blanky + 1] = board[blankx][blanky + 1], board[blankx][blanky]
            self.BoardData.incMovCounter()
        elif move == self.DOWN and self.isValidMove(board, move):
            board[blankx][blanky], board[blankx][blanky - 1] = board[blankx][blanky - 1], board[blankx][blanky]
            self.BoardData.incMovCounter()
        elif move == self.LEFT and self.isValidMove(board, move):
            board[blankx][blanky], board[blankx + 1][blanky] = board[blankx + 1][blanky], board[blankx][blanky]
            self.BoardData.incMovCounter()
        elif move == self.RIGHT and self.isValidMove(board, move):
            board[blankx][blanky], board[blankx - 1][blanky] = board[blankx - 1][blanky], board[blankx][blanky]
            self.BoardData.incMovCounter()
        return board

    def isValidMove(self, board, move):
        blankx, blanky = self.getBlankPosition(board)
        return (move == self.UP and blanky != len(board[0]) - 1) or \
               (move == self.DOWN and blanky != 0) or \
               (move == self.LEFT and blankx != len(board) - 1) or \
               (move == self.RIGHT and blankx != 0)

    def getRandomMove(self, board, lastMove=None):
        # start with a full list of all four moves
        validMoves = [self.UP, self.DOWN, self.LEFT, self.RIGHT]

        # remove moves from the list as they are disqualified
        if lastMove == self.UP or not self.isValidMove(board, self.DOWN):
            validMoves.remove(self.DOWN)
        if lastMove == self.DOWN or not self.isValidMove(board, self.UP):
            validMoves.remove(self.UP)
        if lastMove == self.LEFT or not self.isValidMove(board, self.RIGHT):
            validMoves.remove(self.RIGHT)
        if lastMove == self.RIGHT or not self.isValidMove(board, self.LEFT):
            validMoves.remove(self.LEFT)
        # return a random move from the list of remaining moves
        return random.choice(validMoves)

    def getLeftTopOfTile(self, tileX, tileY):
        left = self.XMARGIN + (tileX * self.BoardData.getTILESIZE()) + (tileX - 1)
        top = self.YMARGIN + (tileY * self.BoardData.getTILESIZE()) + (tileY - 1)
        return (left, top)

    def getSpotClicked(self, x, y):
        # from the x & y pixel coordinates, get the x & y board coordinates
        for tileX in range(self.BoardData.getBOARDERSIZE()):
            for tileY in range(self.BoardData.getBOARDERSIZE()):
                left, top = self.getLeftTopOfTile(tileX, tileY)
                tileRect = pygame.Rect(left, top, self.BoardData.getTILESIZE(), self.BoardData.getTILESIZE())
                if tileRect.collidepoint(x, y):
                    return (tileX, tileY)
        return (None, None)

    def drawTile(self, tilex, tiley, number, adjx=0, adjy=0):
        # draw a tile at board coordinates tilex and tiley, optionally a few
        # pixels over (determined by adjx and adjy)
        left, top = self.getLeftTopOfTile(tilex, tiley)
        pygame.draw.rect(DISPLAYSURF, self.TILECOLOR,
                         (left + adjx, top + adjy, self.BoardData.getTILESIZE(), self.BoardData.getTILESIZE()))
        textSurf = BASICFONT.render(str(number), True, self.TEXTCOLOR)
        textRect = textSurf.get_rect()
        textRect.center = left + int(self.BoardData.getTILESIZE() / 2) + adjx, top + int(
            self.BoardData.getTILESIZE() / 2) + adjy
        DISPLAYSURF.blit(textSurf, textRect)

    def makeText(self, text, color, bgcolor, top, left):
        # create the Surface and Rect objects for some text.
        textSurf = BASICFONT.render(text, True, color, bgcolor)
        textRect = textSurf.get_rect()
        textRect.topleft = (top, left)
        return (textSurf, textRect)

    def drawBoard(self, board, message):
        DISPLAYSURF.fill(self.BGCOLOR)
        if message:
            textSurf, textRect = self.makeText(message, self.MESSAGECOLOR, self.BGCOLOR, 5, 5)
            DISPLAYSURF.blit(textSurf, textRect)

        for tilex in range(self.BoardData.getBOARDERSIZE()):
            for tiley in range(self.BoardData.getBOARDERSIZE()):
                if board[tilex][tiley]:
                    self.drawTile(tilex, tiley, board[tilex][tiley])

        # Draw the board border (Blue line around the tiles) \\Kamel
        left, top = self.getLeftTopOfTile(0, 0)
        width = 250
        height = 250
        pygame.draw.rect(DISPLAYSURF, self.BORDERCOLOR, (left - 5, top - 5, width + 11, height + 11), 4)

        DISPLAYSURF.blit(RESET_SURF, RESET_RECT)
        DISPLAYSURF.blit(NEW_SURF, NEW_RECT)
        DISPLAYSURF.blit(SOLVE_SURF, SOLVE_RECT)
        DISPLAYSURF.blit(S3_SURF, S3_RECT)
        DISPLAYSURF.blit(S4_SURF, S4_RECT)
        DISPLAYSURF.blit(S5_SURF, S5_RECT)
        DISPLAYSURF.blit(H1_SURF, H1_RECT)
        DISPLAYSURF.blit(Euclidean_SURF, Euclidean_RECT)
        DISPLAYSURF.blit(H3_SURF, H3_RECT)
        DISPLAYSURF.blit(H4_SURF, H4_RECT)
        DISPLAYSURF.blit(H5_SURF, H5_RECT)

        DISPLAYSURF.blit(counterTextSURF, counterTextRECT)
        counterSURF, counterRECT = self.makeText(str(self.BoardData.getMovCounter()), self.MESSAGECOLOR, self.BGCOLOR,
                                                 190, 30)
        DISPLAYSURF.blit(counterSURF, counterRECT)

    def slideAnimation(self, board, direction, message, animationSpeed):
        # Note: This function does not check if the move is valid.

        blankx, blanky = self.getBlankPosition(board)
        if direction == self.UP:
            movex = blankx
            movey = blanky + 1
        elif direction == self.DOWN:
            movex = blankx
            movey = blanky - 1
        elif direction == self.LEFT:
            movex = blankx + 1
            movey = blanky
        elif direction == self.RIGHT:
            movex = blankx - 1
            movey = blanky

        # prepare the base surface
        self.drawBoard(board, message)
        baseSurf = DISPLAYSURF.copy()
        # draw a blank space over the moving tile on the baseSurf Surface.
        moveLeft, moveTop = self.getLeftTopOfTile(movex, movey)
        pygame.draw.rect(baseSurf, self.BGCOLOR,
                         (moveLeft, moveTop, self.BoardData.getTILESIZE(), self.BoardData.getTILESIZE()))

        for i in range(0, self.BoardData.getTILESIZE(), animationSpeed):
            # animate the tile sliding over
            self.checkForQuit()
            DISPLAYSURF.blit(baseSurf, (0, 0))
            if direction == self.UP:
                self.drawTile(movex, movey, board[movex][movey], 0, -i)
            if direction == self.DOWN:
                self.drawTile(movex, movey, board[movex][movey], 0, i)
            if direction == self.LEFT:
                self.drawTile(movex, movey, board[movex][movey], -i, 0)
            if direction == self.RIGHT:
                self.drawTile(movex, movey, board[movex][movey], i, 0)

            pygame.display.update()
            DISPLAYSURF.blit(counterTextSURF, counterTextRECT)
            counterSURF, counterRECT = self.makeText(str(self.BoardData.getMovCounter()), self.MESSAGECOLOR,
                                                     self.BGCOLOR, 190, 30)
            DISPLAYSURF.blit(counterSURF, counterRECT)
            FPSCLOCK.tick(self.FPS)

    def generateNewPuzzle(self, numSlides):
        # From a starting configuration, make numSlides number of moves (and
        # animate these moves).
        board = deepcopy(self.BoardData.getBoard())
        self.drawBoard(board, '')
        pygame.display.update()
        pygame.time.wait(500)  # pause 500 milliseconds for effect
        lastMove = None
        for i in range(numSlides):
            move = self.getRandomMove(board, lastMove)
            self.slideAnimation(board, move, 'Generating new puzzle...',animationSpeed=int(self.BoardData.getTILESIZE() / 3))
            self.makeMove(board, move)
            self.BoardData.resetMovCounter()
            lastMove = move
            self.allMoves.append(move)
        return board

    def correctsoltion(self, moves):
        # print(moves)
        correctsolution = list()
        for move in moves:
            if move == self.UP:
                correctsolution.append(self.DOWN)
            elif move == self.DOWN:
                correctsolution.append(self.UP)
            elif move == self.RIGHT:
                correctsolution.append(self.LEFT)
            elif move == self.LEFT:
                correctsolution.append(self.RIGHT)
        return correctsolution

    def resetAnimation(self, board, moves):
        # make all of the moves in allMoves in reverse.
        for move in moves:
            if move == self.UP:
                oppositeMove = self.DOWN
            elif move == self.DOWN:
                oppositeMove = self.UP
            elif move == self.RIGHT:
                oppositeMove = self.LEFT
            elif move == self.LEFT:
                oppositeMove = self.RIGHT
            # print(oppositeMove)
            self.slideAnimation(board, oppositeMove, '', animationSpeed=int(self.BoardData.getTILESIZE() / 2))
            self.BoardData.resetMovCounter()
            self.makeMove(board, oppositeMove)

    def creatSearchSpace(self, state, heuristicF, parent=-1, lastmove=None):
        # print(self.key)
        if state == self.Goal:
            print("Solved")
            self.Space.update({self.key: [deepcopy(state), heuristicF(state), lastmove, parent]})
            self.BoardData.setSearchSpace(self.Space)
        else:
            if self.key == 0:
                self.Space.update({self.key: [deepcopy(state), heuristicF(state), lastmove, parent]})
                parent = self.key
                self.key += 1
            self.CloseList.append(state)
            possiblestates = self.nextstate(state, lastmove)  # possiblestates is a list of [boardstate, lastmove]
            for pstate in possiblestates:
                if pstate[0] not in self.CloseList:
                    heuristicvalue = heuristicF(pstate[0])  # pstate[0] represent boardstate
                    self.Space.update({self.key: [deepcopy(pstate[0]), heuristicvalue, pstate[1], parent]})
                    self.Fronte.append([heuristicvalue, self.key, pstate[1]])
                    self.key += 1
            self.Fronte = sorted(self.Fronte, key=itemgetter(0), reverse=True)
            NextState = self.Fronte.pop()
            self.creatSearchSpace(self.Space.get(NextState[1])[0], heuristicF, parent = NextState[1], lastmove = NextState[2])  # NextState[1] represent boardstate NextState[2] represent lastmove

    def nextstate(self, board, lastMove):
        validMoves = [self.UP, self.DOWN, self.LEFT, self.RIGHT]
        nextstates = []
        # remove moves from the list as they are disqualified
        if lastMove == self.UP or not self.isValidMove(board, self.DOWN):
            validMoves.remove(self.DOWN)
        if lastMove == self.DOWN or not self.isValidMove(board, self.UP):
            validMoves.remove(self.UP)
        if lastMove == self.LEFT or not self.isValidMove(board, self.RIGHT):
            validMoves.remove(self.RIGHT)
        if lastMove == self.RIGHT or not self.isValidMove(board, self.LEFT):
            validMoves.remove(self.LEFT)
        for move in validMoves:
            # print(board)
            # print(nextstates)
            # print('#'*20)
            nextstates.append([self.makeMove(deepcopy(board), move), move])
        return nextstates


if __name__ == '__main__':
    GUI().main()
