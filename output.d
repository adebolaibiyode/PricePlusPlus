
Price Rule: "Mult[Minus[ProductA,0.04],Minus[ProductB,0.05],SUM[ProductC,0.06]]"
Parser:
Parent Dictionary: {0: ['mult', 'mult_0'],
					1: ['minus', 'minus_1'], 
					2: ['minus', 'minus_3'],
					3: ['sum', 'sum_5']}
Child Dictionary: {0: [0, 'minus_1'], 
					1: [1, 'producta,0.04'], 
					2: [0, 'minus_3'],
					3: [2, 'productb,0.05'],
					4: [0, 'sum_5'],
					5: [3, 'productc,0.06']}

Price Rule: "Mult[Minus[ProductA,0.04],Minus[ProductB,0.05],SUM[ProductC,0.06],Divide[Sum[ProductD,3.0],5.55]]"
Parser:
Parent Dictionary: {0: ['mult', 'mult_0'],
					1: ['minus', 'minus_1'],
					2: ['minus', 'minus_3'],
					3: ['sum', 'sum_5'], 
					4: ['divide', 'divide_7'], 
					5: ['sum', 'sum_8']}
Child Dictionary: {0: [0, 'minus_1'],
					1: [1, 'producta,0.04'],
					2: [0, 'minus_3'],
					3: [2, 'productb,0.05'],
					4: [0, 'sum_5'],
					5: [3, 'productc,0.06'],
					6: [0, 'divide_7'],
					7: [4, 'sum_8'], 
					8: [5, 'productd,3.0'],
					9: [4, '5.55']}