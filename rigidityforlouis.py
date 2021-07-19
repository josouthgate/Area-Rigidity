# Inputs an edge set E and a configuration matrix P (with bottom row all 1s), outputs the area rigidity matrix

def rigmat2(E,P): #I got an error using matrix_from_rows_and_columns so I had to improvise the cross product, will fix this for higher dimensions theough
	n = P.ncols()
	m = len(E)
	Prows = P.rows()
	R = []
	for e in E:
		MatRow = []
		for i in range(n):
			for coord in range(2):
				if i not in e:
					MatRow.append(0)
				else:
					for projn in range(2):
						if projn != coord:
							L = projn
					OppEdge = []
					for j in e:
						if j != i:
							OppEdge.append(j)
					minor = P[L,OppEdge[0]] - P[L,OppEdge[1]]
					if (coord == 0 and i > OppEdge[0] and i < OppEdge[1]) or (coord == 1 and i < OppEdge[0] and i < OppEdge[1]) or (coord == 1 and i > OppEdge[0] and i > OppEdge[1]):
						MatRow.append(-minor)
					else:
						MatRow.append(minor)
		R.append(MatRow)
	return(matrix(R))

# Inputs an edge set E, the number of vertices n, and an element stress of the cokernel (kernel in Sage) of the rigidity matrix, outputs the corresponding stress matrix and the one skeleton of the graph

def stressmat2(E,n,stress): # OneSkel is returned so we know the indexing of the columns of the stess matrix
	OneSkel = []	
	OneSkelReps = []
	Stress = []
	for e in E:
		Subs = Subsets(e,2)
		for i in Subs:
			OneSkelReps.append(list(i))
	for i in OneSkelReps:
		if i not in OneSkel:
			OneSkel.append(i)
	for i in range(n):
		MatRow = []
		for OppEdge in OneSkel:
			L0 = []
			L1 = []
			L2 = []
			for j in OppEdge:
				L0.append(j)
				L1.append(j)
				L2.append(j)
			if i in OppEdge:
				MatRow.append(0)
			else:
				L0.insert(0,i)
				L1.insert(1,i)
				L2.insert(2,i)
				if L0 in E:
					MatRow.append(stress[E.index(L0)])
				elif L1 in E:
					MatRow.append(-stress[E.index(L1)])
				elif L2 in E:
					MatRow.append(stress[E.index(L2)])
				else:
					MatRow.append(0)
		Stress.append(MatRow)
	return([matrix(Stress),OneSkel])

# Inputs the configuration matrix and one skeleton of the graph, outputs the edge-direction matrix

def distmat2(P,OneSkel):
	s = len(OneSkel)
	D = []
	for coord in range(2):
		DRow = []
		for Edge in OneSkel:
			DRow.append(P[coord,Edge[1]]-P[coord,Edge[0]])
		D.append(DRow)
	return(matrix(D))