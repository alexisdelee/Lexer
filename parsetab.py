
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftPLUSMINUSleftTIMESDIVIDEREMAINDERrightUMINUSleftEXPONENTADDRESS COLON CONST DEF DELETE DIFFERENT DIVIDE DO DOUBLE_EQUALS ELSE END EQUALS EXPONENT FOR IF INFERIOR INFERIOR_OR_EQUAL LPAREN LSQUARE MINUS NEXT NUMBER PLUS PRINT QUOTE REMAINDER RPAREN RSQUARE SEMICOLON SEPARATOR STRING SUPERIOR SUPERIOR_OR_EQUAL THEN TIMES TO TYPEOF VAR VARIABLE WHILEscope : blockblock : block statement\n             | statementstatement : IF LPAREN comparison RPAREN THEN block END\n                 | IF LPAREN comparison RPAREN THEN block ELSE block ENDstatement : FOR LPAREN expression TO expression RPAREN NEXT block ENDstatement : WHILE LPAREN comparison RPAREN NEXT block ENDstatement : PRINT LPAREN expression RPAREN SEMICOLONstatement : VARIABLE EQUALS expression SEMICOLON\n                 | VARIABLE EQUALS ADDRESS VARIABLE SEMICOLONstatement : ADDRESS VARIABLE EQUALS expression SEMICOLONstatement : VARIABLE LSQUARE expression RSQUARE EQUALS expression SEMICOLON\n                 | ADDRESS VARIABLE LSQUARE expression RSQUARE EQUALS expression SEMICOLONstatement : VAR VARIABLE EQUALS expression SEMICOLON\n                 | VAR VARIABLE EQUALS ADDRESS VARIABLE SEMICOLONstatement : CONST VARIABLE EQUALS expression SEMICOLON\n                 | CONST VARIABLE EQUALS ADDRESS VARIABLE SEMICOLON\n                 | CONST VARIABLE EQUALS LSQUARE cargument RSQUARE SEMICOLONstatement : DEF VARIABLE LPAREN dargument RPAREN DO block END\n                 | DEF VARIABLE LPAREN RPAREN DO block ENDstatement : VARIABLE LPAREN cargument RPAREN SEMICOLON\n                 | VARIABLE LPAREN RPAREN SEMICOLONdargument : dargument SEPARATOR VARIABLE\n                 | VARIABLEcargument : cargument SEPARATOR expression\n                 | expressionstatement : DELETE VARIABLE SEMICOLONstatement : expression SEMICOLONcomparison : expression INFERIOR expression\n                  | expression INFERIOR_OR_EQUAL expression\n                  | expression SUPERIOR expression\n                  | expression SUPERIOR_OR_EQUAL expression\n                  | expression DOUBLE_EQUALS expression\n                  | expression DIFFERENT expressionexpression : expression PLUS expression\n                  | expression MINUS expression\n                  | expression TIMES expression\n                  | expression DIVIDE expression\n                  | expression EXPONENT expression\n                  | expression REMAINDER expression\n                  | expression INFERIOR expression\n                  | expression INFERIOR_OR_EQUAL expression\n                  | expression SUPERIOR expression\n                  | expression SUPERIOR_OR_EQUAL expression\n                  | expression DOUBLE_EQUALS expression\n                  | expression DIFFERENT expressionexpression : MINUS expression %prec UMINUSexpression : LPAREN expression RPARENexpression : TYPEOF LPAREN VARIABLE RPARENexpression : VARIABLE LSQUARE expression RSQUAREexpression : VARIABLE LSQUARE expression COLON expression RSQUARE\n                  | VARIABLE LSQUARE COLON expression RSQUARE\n                  | VARIABLE LSQUARE expression COLON RSQUARE\n                  | VARIABLE LSQUARE COLON RSQUAREexpression : NUMBERexpression : STRINGexpression : LSQUARE cargument RSQUAREexpression : VARIABLE'
    
_lr_action_items = {'IF':([0,2,3,21,26,85,98,105,118,127,128,129,134,135,137,139,144,145,147,151,152,154,156,157,158,159,160,161,163,164,165,166,167,168,169,170,171,],[4,4,-3,-2,-28,-27,-9,-22,4,4,-8,-10,-21,-11,-14,-16,4,4,4,-15,-17,4,4,-4,4,4,-7,-12,-18,4,-20,4,4,-13,-19,-5,-6,]),'FOR':([0,2,3,21,26,85,98,105,118,127,128,129,134,135,137,139,144,145,147,151,152,154,156,157,158,159,160,161,163,164,165,166,167,168,169,170,171,],[6,6,-3,-2,-28,-27,-9,-22,6,6,-8,-10,-21,-11,-14,-16,6,6,6,-15,-17,6,6,-4,6,6,-7,-12,-18,6,-20,6,6,-13,-19,-5,-6,]),'WHILE':([0,2,3,21,26,85,98,105,118,127,128,129,134,135,137,139,144,145,147,151,152,154,156,157,158,159,160,161,163,164,165,166,167,168,169,170,171,],[8,8,-3,-2,-28,-27,-9,-22,8,8,-8,-10,-21,-11,-14,-16,8,8,8,-15,-17,8,8,-4,8,8,-7,-12,-18,8,-20,8,8,-13,-19,-5,-6,]),'PRINT':([0,2,3,21,26,85,98,105,118,127,128,129,134,135,137,139,144,145,147,151,152,154,156,157,158,159,160,161,163,164,165,166,167,168,169,170,171,],[9,9,-3,-2,-28,-27,-9,-22,9,9,-8,-10,-21,-11,-14,-16,9,9,9,-15,-17,9,9,-4,9,9,-7,-12,-18,9,-20,9,9,-13,-19,-5,-6,]),'VARIABLE':([0,2,3,5,11,12,13,14,15,16,17,21,22,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,52,56,73,75,78,79,81,82,83,84,85,88,89,90,91,92,93,95,98,101,105,110,112,113,118,127,128,129,130,134,135,137,139,143,144,145,147,150,151,152,154,156,157,158,159,160,161,163,164,165,166,167,168,169,170,171,],[10,10,-3,24,44,24,47,48,49,50,24,-2,24,24,-28,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,86,24,99,24,24,24,24,24,24,114,-27,24,24,24,24,24,24,24,-9,24,-22,138,140,24,10,10,-8,-10,24,-21,-11,-14,-16,155,10,10,10,24,-15,-17,10,10,-4,10,10,-7,-12,-18,10,-20,10,10,-13,-19,-5,-6,]),'ADDRESS':([0,2,3,21,26,41,82,83,85,98,105,118,127,128,129,134,135,137,139,144,145,147,151,152,154,156,157,158,159,160,161,163,164,165,166,167,168,169,170,171,],[11,11,-3,-2,-28,73,110,112,-27,-9,-22,11,11,-8,-10,-21,-11,-14,-16,11,11,11,-15,-17,11,11,-4,11,11,-7,-12,-18,11,-20,11,11,-13,-19,-5,-6,]),'VAR':([0,2,3,21,26,85,98,105,118,127,128,129,134,135,137,139,144,145,147,151,152,154,156,157,158,159,160,161,163,164,165,166,167,168,169,170,171,],[13,13,-3,-2,-28,-27,-9,-22,13,13,-8,-10,-21,-11,-14,-16,13,13,13,-15,-17,13,13,-4,13,13,-7,-12,-18,13,-20,13,13,-13,-19,-5,-6,]),'CONST':([0,2,3,21,26,85,98,105,118,127,128,129,134,135,137,139,144,145,147,151,152,154,156,157,158,159,160,161,163,164,165,166,167,168,169,170,171,],[14,14,-3,-2,-28,-27,-9,-22,14,14,-8,-10,-21,-11,-14,-16,14,14,14,-15,-17,14,14,-4,14,14,-7,-12,-18,14,-20,14,14,-13,-19,-5,-6,]),'DEF':([0,2,3,21,26,85,98,105,118,127,128,129,134,135,137,139,144,145,147,151,152,154,156,157,158,159,160,161,163,164,165,166,167,168,169,170,171,],[15,15,-3,-2,-28,-27,-9,-22,15,15,-8,-10,-21,-11,-14,-16,15,15,15,-15,-17,15,15,-4,15,15,-7,-12,-18,15,-20,15,15,-13,-19,-5,-6,]),'DELETE':([0,2,3,21,26,85,98,105,118,127,128,129,134,135,137,139,144,145,147,151,152,154,156,157,158,159,160,161,163,164,165,166,167,168,169,170,171,],[16,16,-3,-2,-28,-27,-9,-22,16,16,-8,-10,-21,-11,-14,-16,16,16,16,-15,-17,16,16,-4,16,16,-7,-12,-18,16,-20,16,16,-13,-19,-5,-6,]),'MINUS':([0,2,3,5,7,10,12,17,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,46,51,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,71,72,74,75,78,79,80,81,82,83,85,88,89,90,91,92,93,94,95,98,100,101,102,103,105,106,107,108,109,111,113,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,137,139,144,145,147,148,149,150,151,152,153,154,156,157,158,159,160,161,162,163,164,165,166,167,168,169,170,171,],[17,17,-3,17,28,-58,17,17,-55,-56,-2,17,28,-58,17,-28,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,28,-47,28,-48,17,28,-35,-36,-37,-38,-39,-40,28,28,28,28,28,28,28,28,28,17,17,17,-57,17,17,17,-27,17,17,17,17,17,17,28,17,-9,-50,17,28,-54,-22,28,28,28,28,28,17,-49,17,28,28,28,28,28,28,-50,28,17,-8,-10,17,28,-53,-52,-21,-11,-14,-16,17,17,17,28,-51,17,-15,-17,-57,17,17,-4,17,17,-7,-12,28,-18,17,-20,17,17,-13,-19,-5,-6,]),'LPAREN':([0,2,3,4,5,6,8,9,10,12,17,18,21,22,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,49,56,75,78,79,81,82,83,85,88,89,90,91,92,93,95,98,101,105,113,118,127,128,129,130,134,135,137,139,144,145,147,150,151,152,154,156,157,158,159,160,161,163,164,165,166,167,168,169,170,171,],[5,5,-3,22,5,25,39,40,43,5,5,52,-2,5,5,-28,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,84,5,5,5,5,5,5,5,-27,5,5,5,5,5,5,5,-9,5,-22,5,5,5,-8,-10,5,-21,-11,-14,-16,5,5,5,5,-15,-17,5,5,-4,5,5,-7,-12,-18,5,-20,5,5,-13,-19,-5,-6,]),'TYPEOF':([0,2,3,5,12,17,21,22,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,56,75,78,79,81,82,83,85,88,89,90,91,92,93,95,98,101,105,113,118,127,128,129,130,134,135,137,139,144,145,147,150,151,152,154,156,157,158,159,160,161,163,164,165,166,167,168,169,170,171,],[18,18,-3,18,18,18,-2,18,18,-28,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,-27,18,18,18,18,18,18,18,-9,18,-22,18,18,18,-8,-10,18,-21,-11,-14,-16,18,18,18,18,-15,-17,18,18,-4,18,18,-7,-12,-18,18,-20,18,18,-13,-19,-5,-6,]),'NUMBER':([0,2,3,5,12,17,21,22,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,56,75,78,79,81,82,83,85,88,89,90,91,92,93,95,98,101,105,113,118,127,128,129,130,134,135,137,139,144,145,147,150,151,152,154,156,157,158,159,160,161,163,164,165,166,167,168,169,170,171,],[19,19,-3,19,19,19,-2,19,19,-28,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,-27,19,19,19,19,19,19,19,-9,19,-22,19,19,19,-8,-10,19,-21,-11,-14,-16,19,19,19,19,-15,-17,19,19,-4,19,19,-7,-12,-18,19,-20,19,19,-13,-19,-5,-6,]),'STRING':([0,2,3,5,12,17,21,22,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,56,75,78,79,81,82,83,85,88,89,90,91,92,93,95,98,101,105,113,118,127,128,129,130,134,135,137,139,144,145,147,150,151,152,154,156,157,158,159,160,161,163,164,165,166,167,168,169,170,171,],[20,20,-3,20,20,20,-2,20,20,-28,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,-27,20,20,20,20,20,20,20,-9,20,-22,20,20,20,-8,-10,20,-21,-11,-14,-16,20,20,20,20,-15,-17,20,20,-4,20,20,-7,-12,-18,20,-20,20,20,-13,-19,-5,-6,]),'LSQUARE':([0,2,3,5,10,12,17,21,22,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,56,75,78,79,81,82,83,85,88,89,90,91,92,93,95,98,101,105,113,118,127,128,129,130,134,135,137,139,144,145,147,150,151,152,154,156,157,158,159,160,161,163,164,165,166,167,168,169,170,171,],[12,12,-3,12,42,12,12,-2,12,56,12,-28,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,79,12,12,12,12,12,12,113,-27,12,12,12,12,12,12,12,-9,12,-22,12,12,12,-8,-10,12,-21,-11,-14,-16,12,12,12,12,-15,-17,12,12,-4,12,12,-7,-12,-18,12,-20,12,12,-13,-19,-5,-6,]),'$end':([1,2,3,21,26,85,98,105,128,129,134,135,137,139,151,152,157,160,161,163,165,168,169,170,171,],[0,-1,-3,-2,-28,-27,-9,-22,-8,-10,-21,-11,-14,-16,-15,-17,-4,-7,-12,-18,-20,-13,-19,-5,-6,]),'END':([3,21,26,85,98,105,128,129,134,135,137,139,145,147,151,152,156,157,160,161,163,164,165,166,167,168,169,170,171,],[-3,-2,-28,-27,-9,-22,-8,-10,-21,-11,-14,-16,157,160,-15,-17,165,-4,-7,-12,-18,169,-20,170,171,-13,-19,-5,-6,]),'ELSE':([3,21,26,85,98,105,128,129,134,135,137,139,145,151,152,157,160,161,163,165,168,169,170,171,],[-3,-2,-28,-27,-9,-22,-8,-10,-21,-11,-14,-16,158,-15,-17,-4,-7,-12,-18,-20,-13,-19,-5,-6,]),'SEMICOLON':([7,10,19,20,24,50,51,55,58,59,60,61,62,63,64,65,66,67,68,69,72,77,80,97,99,100,103,104,106,109,111,117,125,132,133,138,140,148,149,153,162,],[26,-58,-55,-56,-58,85,-47,-48,-35,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-46,98,105,-57,128,129,-50,-54,134,135,137,139,-49,-50,-53,-52,151,152,161,-51,163,168,]),'PLUS':([7,10,19,20,23,24,46,51,54,55,57,58,59,60,61,62,63,64,65,66,67,68,69,71,72,74,80,94,100,102,103,106,107,108,109,111,117,119,120,121,122,123,124,125,126,131,132,133,148,149,153,162,],[27,-58,-55,-56,27,-58,27,-47,27,-48,27,-35,-36,-37,-38,-39,-40,27,27,27,27,27,27,27,27,27,-57,27,-50,27,-54,27,27,27,27,27,-49,27,27,27,27,27,27,-50,27,27,-53,-52,27,-51,-57,27,]),'TIMES':([7,10,19,20,23,24,46,51,54,55,57,58,59,60,61,62,63,64,65,66,67,68,69,71,72,74,80,94,100,102,103,106,107,108,109,111,117,119,120,121,122,123,124,125,126,131,132,133,148,149,153,162,],[29,-58,-55,-56,29,-58,29,-47,29,-48,29,29,29,-37,-38,-39,-40,29,29,29,29,29,29,29,29,29,-57,29,-50,29,-54,29,29,29,29,29,-49,29,29,29,29,29,29,-50,29,29,-53,-52,29,-51,-57,29,]),'DIVIDE':([7,10,19,20,23,24,46,51,54,55,57,58,59,60,61,62,63,64,65,66,67,68,69,71,72,74,80,94,100,102,103,106,107,108,109,111,117,119,120,121,122,123,124,125,126,131,132,133,148,149,153,162,],[30,-58,-55,-56,30,-58,30,-47,30,-48,30,30,30,-37,-38,-39,-40,30,30,30,30,30,30,30,30,30,-57,30,-50,30,-54,30,30,30,30,30,-49,30,30,30,30,30,30,-50,30,30,-53,-52,30,-51,-57,30,]),'EXPONENT':([7,10,19,20,23,24,46,51,54,55,57,58,59,60,61,62,63,64,65,66,67,68,69,71,72,74,80,94,100,102,103,106,107,108,109,111,117,119,120,121,122,123,124,125,126,131,132,133,148,149,153,162,],[31,-58,-55,-56,31,-58,31,31,31,-48,31,31,31,31,31,-39,31,31,31,31,31,31,31,31,31,31,-57,31,-50,31,-54,31,31,31,31,31,-49,31,31,31,31,31,31,-50,31,31,-53,-52,31,-51,-57,31,]),'REMAINDER':([7,10,19,20,23,24,46,51,54,55,57,58,59,60,61,62,63,64,65,66,67,68,69,71,72,74,80,94,100,102,103,106,107,108,109,111,117,119,120,121,122,123,124,125,126,131,132,133,148,149,153,162,],[32,-58,-55,-56,32,-58,32,-47,32,-48,32,32,32,-37,-38,-39,-40,32,32,32,32,32,32,32,32,32,-57,32,-50,32,-54,32,32,32,32,32,-49,32,32,32,32,32,32,-50,32,32,-53,-52,32,-51,-57,32,]),'INFERIOR':([7,10,19,20,23,24,46,51,54,55,57,58,59,60,61,62,63,64,65,66,67,68,69,71,72,74,80,94,100,102,103,106,107,108,109,111,117,119,120,121,122,123,124,125,126,131,132,133,148,149,153,162,],[33,-58,-55,-56,33,-58,33,-47,88,-48,33,-35,-36,-37,-38,-39,-40,33,33,33,33,33,33,33,33,33,-57,33,-50,33,-54,33,33,33,33,33,-49,33,33,33,33,33,33,-50,33,33,-53,-52,33,-51,-57,33,]),'INFERIOR_OR_EQUAL':([7,10,19,20,23,24,46,51,54,55,57,58,59,60,61,62,63,64,65,66,67,68,69,71,72,74,80,94,100,102,103,106,107,108,109,111,117,119,120,121,122,123,124,125,126,131,132,133,148,149,153,162,],[34,-58,-55,-56,34,-58,34,-47,89,-48,34,-35,-36,-37,-38,-39,-40,34,34,34,34,34,34,34,34,34,-57,34,-50,34,-54,34,34,34,34,34,-49,34,34,34,34,34,34,-50,34,34,-53,-52,34,-51,-57,34,]),'SUPERIOR':([7,10,19,20,23,24,46,51,54,55,57,58,59,60,61,62,63,64,65,66,67,68,69,71,72,74,80,94,100,102,103,106,107,108,109,111,117,119,120,121,122,123,124,125,126,131,132,133,148,149,153,162,],[35,-58,-55,-56,35,-58,35,-47,90,-48,35,-35,-36,-37,-38,-39,-40,35,35,35,35,35,35,35,35,35,-57,35,-50,35,-54,35,35,35,35,35,-49,35,35,35,35,35,35,-50,35,35,-53,-52,35,-51,-57,35,]),'SUPERIOR_OR_EQUAL':([7,10,19,20,23,24,46,51,54,55,57,58,59,60,61,62,63,64,65,66,67,68,69,71,72,74,80,94,100,102,103,106,107,108,109,111,117,119,120,121,122,123,124,125,126,131,132,133,148,149,153,162,],[36,-58,-55,-56,36,-58,36,-47,91,-48,36,-35,-36,-37,-38,-39,-40,36,36,36,36,36,36,36,36,36,-57,36,-50,36,-54,36,36,36,36,36,-49,36,36,36,36,36,36,-50,36,36,-53,-52,36,-51,-57,36,]),'DOUBLE_EQUALS':([7,10,19,20,23,24,46,51,54,55,57,58,59,60,61,62,63,64,65,66,67,68,69,71,72,74,80,94,100,102,103,106,107,108,109,111,117,119,120,121,122,123,124,125,126,131,132,133,148,149,153,162,],[37,-58,-55,-56,37,-58,37,-47,92,-48,37,-35,-36,-37,-38,-39,-40,37,37,37,37,37,37,37,37,37,-57,37,-50,37,-54,37,37,37,37,37,-49,37,37,37,37,37,37,-50,37,37,-53,-52,37,-51,-57,37,]),'DIFFERENT':([7,10,19,20,23,24,46,51,54,55,57,58,59,60,61,62,63,64,65,66,67,68,69,71,72,74,80,94,100,102,103,106,107,108,109,111,117,119,120,121,122,123,124,125,126,131,132,133,148,149,153,162,],[38,-58,-55,-56,38,-58,38,-47,93,-48,38,-35,-36,-37,-38,-39,-40,38,38,38,38,38,38,38,38,38,-57,38,-50,38,-54,38,38,38,38,38,-49,38,38,38,38,38,38,-50,38,38,-53,-52,38,-51,-57,38,]),'EQUALS':([10,44,47,48,100,136,],[41,78,82,83,130,150,]),'RPAREN':([19,20,23,24,43,46,51,53,55,58,59,60,61,62,63,64,65,66,67,68,69,70,71,76,80,84,86,103,108,114,115,117,119,120,121,122,123,124,125,126,132,133,149,155,],[-55,-56,55,-58,77,-26,-47,87,-48,-35,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-46,96,97,104,-57,116,117,-54,-25,-24,142,-49,-29,-30,-31,-32,-33,-34,-50,146,-53,-52,-51,-23,]),'RSQUARE':([19,20,24,45,46,51,55,58,59,60,61,62,63,64,65,66,67,68,69,74,75,80,94,101,102,103,107,108,117,125,131,132,133,141,149,],[-55,-56,-58,80,-26,-47,-48,-35,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-46,100,103,-57,125,132,133,-54,136,-25,-49,-50,149,-53,-52,153,-51,]),'SEPARATOR':([19,20,24,45,46,51,55,58,59,60,61,62,63,64,65,66,67,68,69,76,80,103,108,114,115,117,125,132,133,141,149,155,],[-55,-56,-58,81,-26,-47,-48,-35,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-46,81,-57,-54,-25,-24,143,-49,-50,-53,-52,81,-51,-23,]),'TO':([19,20,24,51,55,57,58,59,60,61,62,63,64,65,66,67,68,69,80,103,117,125,132,133,149,],[-55,-56,-58,-47,-48,95,-35,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-46,-57,-54,-49,-50,-53,-52,-51,]),'COLON':([19,20,24,42,51,55,56,58,59,60,61,62,63,64,65,66,67,68,69,74,80,94,103,117,125,132,133,149,],[-55,-56,-58,75,-47,-48,75,-35,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-46,101,-57,101,-54,-49,-50,-53,-52,-51,]),'THEN':([87,],[118,]),'NEXT':([96,146,],[127,159,]),'DO':([116,142,],[144,154,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'scope':([0,],[1,]),'block':([0,118,127,144,154,158,159,],[2,145,147,156,164,166,167,]),'statement':([0,2,118,127,144,145,147,154,156,158,159,164,166,167,],[3,21,3,3,3,21,21,3,21,3,3,21,21,21,]),'expression':([0,2,5,12,17,22,25,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,56,75,78,79,81,82,83,88,89,90,91,92,93,95,101,113,118,127,130,144,145,147,150,154,156,158,159,164,166,167,],[7,7,23,46,51,54,57,58,59,60,61,62,63,64,65,66,67,68,69,54,71,72,74,46,94,102,106,107,108,109,111,119,120,121,122,123,124,126,131,46,7,7,148,7,7,7,162,7,7,7,7,7,7,7,]),'cargument':([12,43,113,],[45,76,141,]),'comparison':([22,39,],[53,70,]),'dargument':([84,],[115,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> scope","S'",1,None,None,None),
  ('scope -> block','scope',1,'p_scope','main.py',169),
  ('block -> block statement','block',2,'p_block','main.py',177),
  ('block -> statement','block',1,'p_block','main.py',178),
  ('statement -> IF LPAREN comparison RPAREN THEN block END','statement',7,'p_statement_condition','main.py',186),
  ('statement -> IF LPAREN comparison RPAREN THEN block ELSE block END','statement',9,'p_statement_condition','main.py',187),
  ('statement -> FOR LPAREN expression TO expression RPAREN NEXT block END','statement',9,'p_statement_for','main.py',195),
  ('statement -> WHILE LPAREN comparison RPAREN NEXT block END','statement',7,'p_statement_while','main.py',199),
  ('statement -> PRINT LPAREN expression RPAREN SEMICOLON','statement',5,'p_statement_print','main.py',203),
  ('statement -> VARIABLE EQUALS expression SEMICOLON','statement',4,'p_statement_assign','main.py',207),
  ('statement -> VARIABLE EQUALS ADDRESS VARIABLE SEMICOLON','statement',5,'p_statement_assign','main.py',208),
  ('statement -> ADDRESS VARIABLE EQUALS expression SEMICOLON','statement',5,'p_statement_assign_pointer','main.py',216),
  ('statement -> VARIABLE LSQUARE expression RSQUARE EQUALS expression SEMICOLON','statement',7,'p_statement_assign_element','main.py',220),
  ('statement -> ADDRESS VARIABLE LSQUARE expression RSQUARE EQUALS expression SEMICOLON','statement',8,'p_statement_assign_element','main.py',221),
  ('statement -> VAR VARIABLE EQUALS expression SEMICOLON','statement',5,'p_statement_define','main.py',229),
  ('statement -> VAR VARIABLE EQUALS ADDRESS VARIABLE SEMICOLON','statement',6,'p_statement_define','main.py',230),
  ('statement -> CONST VARIABLE EQUALS expression SEMICOLON','statement',5,'p_statement_define_constant','main.py',238),
  ('statement -> CONST VARIABLE EQUALS ADDRESS VARIABLE SEMICOLON','statement',6,'p_statement_define_constant','main.py',239),
  ('statement -> CONST VARIABLE EQUALS LSQUARE cargument RSQUARE SEMICOLON','statement',7,'p_statement_define_constant','main.py',240),
  ('statement -> DEF VARIABLE LPAREN dargument RPAREN DO block END','statement',8,'p_statement_define_function','main.py',250),
  ('statement -> DEF VARIABLE LPAREN RPAREN DO block END','statement',7,'p_statement_define_function','main.py',251),
  ('statement -> VARIABLE LPAREN cargument RPAREN SEMICOLON','statement',5,'p_statement_call_function','main.py',259),
  ('statement -> VARIABLE LPAREN RPAREN SEMICOLON','statement',4,'p_statement_call_function','main.py',260),
  ('dargument -> dargument SEPARATOR VARIABLE','dargument',3,'p_statement_define_argument','main.py',268),
  ('dargument -> VARIABLE','dargument',1,'p_statement_define_argument','main.py',269),
  ('cargument -> cargument SEPARATOR expression','cargument',3,'p_statement_call_argument','main.py',277),
  ('cargument -> expression','cargument',1,'p_statement_call_argument','main.py',278),
  ('statement -> DELETE VARIABLE SEMICOLON','statement',3,'p_statement_delete','main.py',289),
  ('statement -> expression SEMICOLON','statement',2,'p_statement_expr','main.py',293),
  ('comparison -> expression INFERIOR expression','comparison',3,'p_comparison_binop','main.py',297),
  ('comparison -> expression INFERIOR_OR_EQUAL expression','comparison',3,'p_comparison_binop','main.py',298),
  ('comparison -> expression SUPERIOR expression','comparison',3,'p_comparison_binop','main.py',299),
  ('comparison -> expression SUPERIOR_OR_EQUAL expression','comparison',3,'p_comparison_binop','main.py',300),
  ('comparison -> expression DOUBLE_EQUALS expression','comparison',3,'p_comparison_binop','main.py',301),
  ('comparison -> expression DIFFERENT expression','comparison',3,'p_comparison_binop','main.py',302),
  ('expression -> expression PLUS expression','expression',3,'p_expression_binop','main.py',306),
  ('expression -> expression MINUS expression','expression',3,'p_expression_binop','main.py',307),
  ('expression -> expression TIMES expression','expression',3,'p_expression_binop','main.py',308),
  ('expression -> expression DIVIDE expression','expression',3,'p_expression_binop','main.py',309),
  ('expression -> expression EXPONENT expression','expression',3,'p_expression_binop','main.py',310),
  ('expression -> expression REMAINDER expression','expression',3,'p_expression_binop','main.py',311),
  ('expression -> expression INFERIOR expression','expression',3,'p_expression_binop','main.py',312),
  ('expression -> expression INFERIOR_OR_EQUAL expression','expression',3,'p_expression_binop','main.py',313),
  ('expression -> expression SUPERIOR expression','expression',3,'p_expression_binop','main.py',314),
  ('expression -> expression SUPERIOR_OR_EQUAL expression','expression',3,'p_expression_binop','main.py',315),
  ('expression -> expression DOUBLE_EQUALS expression','expression',3,'p_expression_binop','main.py',316),
  ('expression -> expression DIFFERENT expression','expression',3,'p_expression_binop','main.py',317),
  ('expression -> MINUS expression','expression',2,'p_expression_uminus','main.py',321),
  ('expression -> LPAREN expression RPAREN','expression',3,'p_expression_group','main.py',325),
  ('expression -> TYPEOF LPAREN VARIABLE RPAREN','expression',4,'p_expression_typeof','main.py',329),
  ('expression -> VARIABLE LSQUARE expression RSQUARE','expression',4,'p_expression_select','main.py',333),
  ('expression -> VARIABLE LSQUARE expression COLON expression RSQUARE','expression',6,'p_expression_substring','main.py',337),
  ('expression -> VARIABLE LSQUARE COLON expression RSQUARE','expression',5,'p_expression_substring','main.py',338),
  ('expression -> VARIABLE LSQUARE expression COLON RSQUARE','expression',5,'p_expression_substring','main.py',339),
  ('expression -> VARIABLE LSQUARE COLON RSQUARE','expression',4,'p_expression_substring','main.py',340),
  ('expression -> NUMBER','expression',1,'p_expression_number','main.py',353),
  ('expression -> STRING','expression',1,'p_expression_string','main.py',357),
  ('expression -> LSQUARE cargument RSQUARE','expression',3,'p_expression_array','main.py',361),
  ('expression -> VARIABLE','expression',1,'p_expression_variable','main.py',365),
]
