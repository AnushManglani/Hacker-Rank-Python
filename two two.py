import math
s = "1844674407370955161674106937111882365071085430405560261026092790186009960985252853765064402969559046455624695217271474139797930007529685824264482073058782076648391351619055042102986574113383200344578589757929931868733441327844982041917746723970516381171568323982794317579807998610345501008899652130606847906255663073214172223323715616252538366448344131768098523799946916468379859578177088483047579320327229475734293036792189718636043847330179466014340038463189508943008496205724668159759037237747788792245498535675607031239995639976648680825923975906526582032462837994195753268665938105581321030972818840265816397736281374726739986666787659948666753771754907668409286105635143120275902562304104187725513747723032497684230019653080386848786186065006191528308813081840900501117522378138618035792858279853022394381967012525845615079380677438317669219470236837179906477475985598217372094136390078377123228155963917938085569707674435584356811923176489970264571492362373784095686656302231454903657293676544"
a = []
for i in range(0, len(s)):
    if s[i] == "0":
        pass
    else:
        for j in range(i+1, len(s)+1):
            k = int(s[i:j])
            # print(k)
            l = math.log(k, 2)
            # print(l)
            m = math.floor(l)
            if l-m == 0 and m <= 800:
                a.append(k)

print(len(a))
