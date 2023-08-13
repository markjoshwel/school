# programming 1: assignment

## validations

-   ```
    MENU
    ====
    [ 1]  Display Total Number of Carparks in 'carpark-information.csv'
    [ 2]  Display All Basement Carparks in 'carpark-information.csv'
    [ 3]  Read Carpark Availability Data File
    [ 4]  Print Total Number of Carparks in the File Read in [3]
    [ 5]  Display Carparks Without Available Lots
    [ 6]  Display Carparks With At Least x% Available Lots
    [ 7]  Display Addresses of Carparks With At Least x% Available Lots
    [ 8]  Display All Carparks at Given Location
    [ 9]  Display Carpark with the Most Parking Lots
    [10]  Create an Output File with Carpark Availability with Addresses and Sort by Lots Available
    [ 0]  Exit
    Enter your input: a
    Unknown integer value 'a', please re-enter your input: 11
    Menu option should be from 0 to 10, please re-enter your input: 1

    Option 1: Display Total Number of Carparks in 'carpark-information.csv'
    Total number of carparks in 'carpark-information.csv': 2199
    ```

-   ```
    Option 3: Read Carpark Availability Data File
    Enter the file name: hello
    Non-existent file, please enter another file name: hello.txt
    Non-existent file, please enter another file name: 1
    Non-existent file, please enter another file name: carpark-availability-renamed.csv
    Timestamp: 2023-06-19T11:10:27+08:00
    ```

-   ```
    Option 6: Display Carparks With At Least x% Available Lots
    Enter the percentage required: abc
    Unknown integer value 'abc', please re-enter the percentage required: 101
    Percentage should be from 0-100 inclusive, please re-enter the percentage required: 95
    Carpark No  Total Lots  Lots Available  Percentage
    SK48                50              50       100.0
    ...                ...             ...         ...
    ```

## sample outputs

```
MENU
====
[ 1]  Display Total Number of Carparks in 'carpark-information.csv'
[ 2]  Display All Basement Carparks in 'carpark-information.csv'
[ 3]  Read Carpark Availability Data File
[ 4]  Print Total Number of Carparks in the File Read in [3]
[ 5]  Display Carparks Without Available Lots
[ 6]  Display Carparks With At Least x% Available Lots
[ 7]  Display Addresses of Carparks With At Least x% Available Lots
[ 8]  Display All Carparks at Given Location
[ 9]  Display Carpark with the Most Parking Lots
[10]  Create an Output File with Carpark Availability with Addresses and Sort by Lots Available
[ 0]  Exit
Enter your input:
```

1.  ```
    Option 1: Display Total Number of Carparks in 'carpark-information.csv'
    Total number of carparks in 'carpark-information.csv': 2199
    ```

2.  ```
    Option 2: Display All Basement Carparks in 'carpark-information.csv'
    Carpark No Carpark Type       Address
    ACB        BASEMENT CAR PARK  BLK 270/271 ALBERT CENTRE BASEMENT CAR PARK
    BBB        BASEMENT CAR PARK  BLK 231 BRAS BASAH BASEMENT CAR PARK
    BM29       BASEMENT CAR PARK  BLK 163 BUKIT MERAH CENTRAL
    BRB1       BASEMENT CAR PARK  BLK 665 BUFFALO ROAD BASEMENT CAR PARK
    B48B       BASEMENT CAR PARK  BLK 547C BEDOK NORTH AVENUE 1
    B8B        BASEMENT CAR PARK  BLK 222 BEDOK NORTH DRIVE
    B91        BASEMENT CAR PARK  BLK 630 BEDOK RESERVOIR ROAD
    CCKC       BASEMENT CAR PARK  BLK 309 CHOA CHU KANG AVENUE 4
    CC12       BASEMENT CAR PARK  BLK 11 CHAI CHEE ROAD
    CK54       BASEMENT CAR PARK  BLK 638-643 CHOA CHU KANG STREET 64
    DRM5       BASEMENT CAR PARK  BLOCK 110 DEPOT ROAD
    DUXM       BASEMENT CAR PARK  BLK 1 CANTONMENT ROAD
    HDBH       BASEMENT CAR PARK  BLK 480 480 LORONG 6 TOA PAYOH
    KAB        BASEMENT CAR PARK  BLK 334 KRETA AYER BASEMENT CAR PARK
    PDJ3       BASEMENT CAR PARK  BLK 399 YUNG SHENG ROAD
    PDL1       BASEMENT CAR PARK  BLK 168 PUNGGOL FIELD
    PDL2       BASEMENT CAR PARK  681 PUNGGOL DR
    PDT8       BASEMENT CAR PARK  BLK 866A TAMPINES ST 83
    PL19       BASEMENT CAR PARK  BLK 186-188,190-192 PUNGGOL CENTRAL
    PL24       BASEMENT CAR PARK  BLK 178 & 193 EDGEFIELD PLAINS
    PL29       BASEMENT CAR PARK  BLK 633 PUNGGOL DRIVE
    PL30       BASEMENT CAR PARK  BLK 170D PUNGGOL EAST
    PL59       BASEMENT CAR PARK  BLK 308 PUNGGOL WALK
    PL65       BASEMENT CAR PARK  BLK 310 PUNGGOL WALK
    PL81       BASEMENT CAR PARK  BLK 421A NORTHSHORE DRIVE
    PL82       BASEMENT CAR PARK  BLK 413A NORTHSHORE DRIVE
    PL83       BASEMENT CAR PARK  BLK 419A NORTHSHORE DRIVE
    SE5L       BASEMENT CAR PARK  BLK 150 SERANGOON NORTH AVENUE 2
    SK27       BASEMENT CAR PARK  BLK 119 RIVERVALE DRIVE
    SK68       BASEMENT CAR PARK  BLK 275 COMPASSVALE LINK
    SK70       BASEMENT CAR PARK  BLK 273 COMPASSVALE LINK
    SK71       BASEMENT CAR PARK  BLK 277 COMPASSVALE LINK
    SK72       BASEMENT CAR PARK  BLK 272 SENGKANG CENTRAL
    WCB        BASEMENT CAR PARK  BLK 261/262/264 WATERLOO BASEMENT CAR PARK
    WCC        BASEMENT CAR PARK  900 SOUTH WOODLANDS DR
    WDB1       BASEMENT CAR PARK  BLK 104 WHAMPOA DRIVE
    W676       BASEMENT CAR PARK  BLK 676 WOODLANDS DRIVE 71
    Y3M        BASEMENT CAR PARK  BLK 115A/115B/115C YISHUN RING ROAD
    Y62M       BASEMENT CAR PARK  BLOCK 342 YISHUN RING ROAD
    Total number: 39
    ```

3.  ```
    Option 3: Read Carpark Availability Data File
    Enter the file name: Timestamp: 2023-06-19T11:10:27+08:00
    ```

4. ```
    Option 4: Print Total Number of Carparks in the File Read in [3]
    Total Number of Carparks in the File: 1931
    ```

5. ```
    Option 5: Display Carparks Without Available Lots
    Carpark Number: BM29
    Carpark Number: Q81
    Carpark Number: C20
    Carpark Number: HG44
    Carpark Number: CY
    Carpark Number: CR29
    Carpark Number: J56
    Carpark Number: J57L
    Carpark Number: KB14
    Carpark Number: U6
    Carpark Number: T42
    Carpark Number: BH1
    Carpark Number: BH2
    Carpark Number: SK44
    Carpark Number: SK40
    Carpark Number: U27
    Carpark Number: TE3
    Carpark Number: TE4
    Carpark Number: U28
    Carpark Number: B7
    Carpark Number: B7A
    Carpark Number: SE11
    Carpark Number: SE22
    Carpark Number: SK50
    Carpark Number: TP31
    Carpark Number: A30
    Carpark Number: NT6L
    Carpark Number: A20
    Carpark Number: SK51
    Carpark Number: HE3
    Carpark Number: TB2
    Carpark Number: JKM
    Carpark Number: AR9
    Carpark Number: J38
    Carpark Number: NT7L
    Carpark Number: U41
    Carpark Number: C27
    Carpark Number: TBC3
    Carpark Number: C26
    Carpark Number: J62
    Carpark Number: Y57
    Carpark Number: S24L
    Carpark Number: SD2
    Carpark Number: SD3
    Carpark Number: W28
    Carpark Number: P5L
    Carpark Number: BE38
    Carpark Number: SM1
    Carpark Number: K2
    Carpark Number: JB2
    Carpark Number: BM6
    Carpark Number: RHS
    Carpark Number: P40L
    Carpark Number: W26
    Carpark Number: W27
    Carpark Number: TP30
    Carpark Number: Q19
    Carpark Number: STM3
    Carpark Number: TB28
    Carpark Number: S30L
    Carpark Number: EPL
    Carpark Number: A52
    Carpark Number: A54
    Carpark Number: SM9
    Carpark Number: SK41
    Carpark Number: BR10
    Carpark Number: EC3
    Carpark Number: BJ15
    Carpark Number: BJ23
    Carpark Number: Q80
    Carpark Number: BL15
    Carpark Number: PL47
    Carpark Number: J25
    Carpark Number: AR2L
    Carpark Number: BKE1
    Carpark Number: BKE9
    Carpark Number: CR1
    Carpark Number: JCML
    Carpark Number: MP14
    Carpark Number: MP15
    Carpark Number: MP16
    Carpark Number: T55
    Carpark Number: HR4
    Carpark Number: T77
    Carpark Number: GM2
    Carpark Number: GM3
    Carpark Number: TJ39
    Carpark Number: AR7L
    Carpark Number: SK55
    Carpark Number: JM2
    Carpark Number: GEML
    Carpark Number: AR1L
    Carpark Number: KU9
    Carpark Number: W56L
    Carpark Number: A51
    Carpark Number: Y29
    Carpark Number: KJML
    Carpark Number: PDR7
    Carpark Number: BL8L
    Carpark Number: SK31
    Carpark Number: SE12
    Carpark Number: KAS
    Carpark Number: BE22
    Carpark Number: J47
    Carpark Number: TPL
    Carpark Number: A33
    Carpark Number: Y79L
    Carpark Number: NTL
    Carpark Number: B65L
    Total number: 109
    ```

6. ```
    Option 6: Display Carparks With At Least x% Available Lots
    Enter the percentage required: 95
    Carpark No  Total Lots  Lots Available  Percentage
    SK48                50              50       100.0
    TBM2               243             242        99.6
    B90                 75              75       100.0
    TJ37               384             384       100.0
    H87L               500             483        96.6
    SK75               167             167       100.0
    SK88               369             369       100.0
    SK78               264             264       100.0
    SPM                719             709        98.6
    KTM6               252             248        98.4
    JM22               538             534        99.3
    P6L                  6               6       100.0
    SK33               546             535        98.0
    TRS                269             262        97.4
    SK9                456             448        98.2
    SK14               444             444       100.0
    SK81               200             200       100.0
    TPM9               852             840        98.6
    TJ29               306             298        97.4
    S28L                 8               8       100.0
    MP4M               302             301        99.7
    P35L                10              10       100.0
    SK5                668             655        98.1
    CC1                 87              87       100.0
    SK18               663             663       100.0
    PL13               375             372        99.2
    SK46               646             642        99.4
    SK47               632             624        98.7
    TM6                809             794        98.1
    SK34              1044            1015        97.2
    DWSV               527             523        99.2
    PM15              1000             996        99.6
    PM4                809             795        98.3
    PM2               1000             992        99.2
    DWST               366             365        99.7
    W72                524             524       100.0
    DRS               1325            1279        96.5
    DSRL                 4               4       100.0
    BM30                40              40       100.0
    TBL               1000             994        99.4
    JS3L              2010            1978        98.4
    Total number: 41
    ```

7. ```
    Option 7: Display Addresses of Carparks With At Least x% Available Lots
    Enter the percentage required: 95
    Carpark No  Total Lots  Lots Available  Percentage  Address
    SK48                50              50       100.0  BLK 321 ANCHORVALE DRIVE
    TBM2               243             242        99.6  BLK 73A TELOK BLANGAH STREET 32
    B90                 75              75       100.0  BLK 35A BEDOK SOUTH AVENUE 2
    TJ37               384             384       100.0  BLK 337 TAH CHING ROAD
    H87L               500             483        96.6  BLK 950 TO 976 HOUGANG AVENUE 9 /STREET 91
    SK75               167             167       100.0  BLK 441 FERNVALE ROAD
    SK88               369             369       100.0  BLK 451 SENGKANG WEST WAY
    SK78               264             264       100.0  BLK 443 FERNVALE ROAD
    SPM                719             709        98.6  BLK 108 SPOTTISWOODE PARK MSCP
    KTM6               252             248        98.4  BLK 127 KIM TIAN ROAD
    JM22               538             534        99.3  BLK 674 JURONG WEST STREET 65
    P6L                  6               6       100.0  BLK 109B PUNGGOL FIELD
    SK33               546             535        98.0  BLK 201 SENGKANG EAST ROAD
    TRS                269             262        97.4  BLK 14 KAMPONG ARANG ROAD
    SK9                456             448        98.2  BLK 146A RIVERVALE CRESCENT
    SK14               444             444       100.0  BLK 142A RIVERVALE DRIVE
    SK81               200             200       100.0  BLK 446 JALAN KAYU
    TPM9               852             840        98.6  BLK 10A LORONG 7 TOA PAYOH
    TJ29               306             298        97.4  BLK 155A YUNG LOH ROAD
    S28L                 8               8       100.0  BLK 489 ADMIRALTY LINK
    MP4M               302             301        99.7  BLK 16A MARINE TERRACE
    P35L                10              10       100.0  PUNGGOL CENTRAL
    SK5                668             655        98.1  BLK 124D RIVERVALE DRIVE
    CC1                 87              87       100.0  BLK 1/2 CHAI CHEE STREET
    SK18               663             663       100.0  BLK 188E RIVERVALE DRIVE
    PL13               375             372        99.2  BLK 131 EDGEDALE PLAINS
    SK46               646             642        99.4  BLK 312 ANCHORVALE LANE
    SK47               632             624        98.7  BLK 310 ANCHORVALE ROAD
    TM6                809             794        98.1  BLK 307A TAMPINES STREET 32
    SK34              1044            1015        97.2  BLK 299 COMPASSVALE STREET
    DWSV               527             523        99.2  BLK 85 DAWSON ROAD
    PM15              1000             996        99.6  BLK 158A PASIR RIS STREET 13
    PM4                809             795        98.3  BLK 231A PASIR RIS DRIVE 4
    PM2               1000             992        99.2  BLK 220A PASIR RIS STREET 21
    DWST               366             365        99.7  BLK 89A DAWSON ROAD
    W72                524             524       100.0  BLK 792A WOODLANDS AVENUE 6
    DRS               1325            1279        96.5  BLK 102A/102B DEPOT ROAD
    DSRL                 4               4       100.0  BLK 38A MARGARET DRIVE
    BM30                40              40       100.0  BLK 164/165 BUKIT MERAH CENTRAL
    TBL               1000             994        99.4  BLK 90B TELOK BLANGAH STREET 31
    JS3L              2010            1978        98.4  BLK 624A JURONG WEST STREET 61
    Total number: 41
    ```

8.  ```
    Option 8: Display All Carparks at Given Location
    Enter a location: ang mo kio
    Carpark No  Total Lots  Lots Available  Percentage  Address
    AK19                 -               -           -  BLOCK 253 ANG MO KIO STREET 21
    AK31                 -               -           -  BLK 302/348 ANG MO KIO STREET 31
    AK52                 -               -           -  BLK 513 ANG MO KIO STREET 53
    AK6                  -               -           -  BLK 728 ANG MO KIO AVENUE 6
    AK83                 -               -           -  BLK 5022 TO 5095 ANG MO KIO INDUSTRIAL PARK 2
    AK9                  -               -           -  ANG MO KIO AVENUE 9
    AM14               350             231        66.0  BLK 227 ANG MO KIO STREET 23
    AM16               115              87        75.7  BLK 256A ANG MO KIO STREET 21
    AM18               451             265        58.8  BLK 308C ANG MO KIO AVENUE 1
    AM19               300             210        70.0  BLK 260 ANG MO KIO STREET 21
    AM20               676             519        76.8  BLK 309B ANG MO KIO STREET 31
    AM22               289             171        59.2  BLK 316B ANG MO KIO STREET 31
    AM32                91              44        48.4  BLK 255A ANG MO KIO STREET 21
    AM43               465             335        72.0  BLK 455 ANG MO KIO STREET 44
    AM46               408             211        51.7  BLK 588 ANG MO KIO STREET 52
    AM51               269             148        55.0  BLK 700 ANG MO KIO AVENUE 6
    AM64               552             411        74.5  BLK 590 ANG MO KIO STREET 51
    AM79               472             343        72.7  BLK 596 ANG MO KIO STREET 52
    AM80               191             118        61.8  BLK 130A ANG MO KIO STREET 12
    AM81               222             170        76.6  BLK 132A ANG MO KIO STREET 12
    AM96               525             363        69.1  BLK 352A ANG MO KIO STREET 32
    A1                   -               -           -  BLK 215 ANG MO KIO STREET 22
    A10                 62              34        54.8  BLK 201/202 ANG MO KIO STREET 22
    A100                64              41        64.1  BLK 650 ANG MO KIO STREET 61
    A11                368             190        51.6  BLK 223/226/226A-226D ANG MO KIO STREET 22
    A12                194             131        67.5  BLK 229/230 ANG MO KIO STREET 22
    A13                154              65        42.2  BLK 232/233 ANG MO KIO STREET 22
    A15                 59               3         5.1  BLK 226E-226H ANG MO KIO STREET 22
    A2                 188             138        73.4  BLK 206/207 ANG MO KIO STREET 22
    A20                 83               0         0.0  BLK 304/307/319 ANG MO KIO STREET 31
    A21                633             453        71.6  BLK 325/326/301 ANG MO KIO STREET 31
    A23                  -               -           -  BLK 347A ANG MO KIO AVENUE 3
    A24                214              80        37.4  BLK 338/340 ANG MO KIO STREET 32
    A25                543             364        67.0  BLK 330/337 ANG MO KIO AVENUE 8
    A26                333             245        73.6  BLK 113/114/118 ANG MO KIO AVENUE 4
    A27                251             173        68.9  BLK 108/109/110 ANG MO KIO STREET 11
    A28                 84              39        46.4  BLK 103/105/107 ANG MO KIO STREET 11
    A29                435             254        58.4  BLK 347 ANG MO KIO AVENUE 3
    A30                 12               0         0.0  BLK 129/134 ANG MO KIO STREET 12
    A30A                 -               -           -  BLK 133 ANG MO KIO STREET 12
    A31                310             181        58.4  BLK 119/128 ANG MO KIO STREET 12
    A31A                 -               -           -  BLK 125/126 ANG MO KIO STREET 12
    A33                  2               0         0.0  BLK 253/254 ANG MO KIO STREET 21
    A34                220             113        51.4  BLK 422/425 ANG MO KIO STREET 42
    A35                555             389        70.1  BLK 426/428/435 ANG MO KIO STREET 43
    A36                680             455        66.9  BLK 436/443/445 ANG MO KIO STREET 43
    A37                193              39        20.2  BLK 446/449/453 ANG MO KIO STREET 43
    A38                938             548        58.4  BLK 407/410/421 ANG MO KIO AVENUE 10
    A39                200             107        53.5  BLK 401/405 ANG MO KIO AVENUE 10
    A4                 337             238        70.6  BLK 217/220 ANG MO KIO AVENUE 1
    A40                520             384        73.8  BLK 471/476 ANG MO KIO STREET 44
    A41                308             215        69.8  BLK 466/470 ANG MO KIO STREET 44
    A42                146              97        66.4  BLK 461/465 ANG MO KIO STREET 44
    A43                141              61        43.3  BLK 457/458/460 ANG MO KIO STREET 44
    A44                157              85        54.1  BLK 459/456 ANG MO KIO STREET 44
    A45                397             281        70.8  BLK 570/578 ANG MO KIO STREET 51
    A47                303             184        60.7  BLK 562/565/560 ANG MO KIO STREET 54
    A48                 66              37        56.1  BLK 571/73 ANG MO KIO STREET 51
    A49                179              99        55.3  BLK 555/559 ANG MO KIO STREET 54
    A50                206             103        50.0  BLK 548/552/556 ANG MO KIO STREET 54
    A51                 35               0         0.0  BLK 252/253A ANG MO KIO STREET 21
    A52                150               0         0.0  BLK 701/716 ANG MO KIO AVENUE 3/6
    A52L                 -               -           -  BLK 700B/ 700C ANG MO KIO AVENUE 3/6
    A53                757             580        76.6  BLK 712A ANG MO KIO AVENUE 3/6
    A54                767               0         0.0  BLK 727/728 ANG MO KIO AVENUE 6
    A55                767             304        39.6  BLK 729/730 ANG MO KIO AVENUE 6/8
    A56                  -               -           -  BLK 725/730 ANG MO KIO AVENUE 8
    A57                  -               -           -  BLK 720/723 ANG MO KIO AVENUE 8
    A58                  -               -           -  BLK 721/722 ANG MO KIO AVENUE 8
    A59                172             101        58.7  BLK 547/551 ANG MO KIO STREET 54
    A60                517             359        69.4  BLK 540/546 ANG MO KIO STREET 54
    A61               1129             658        58.3  BLK 520/534/529 ANG MO KIO AVENUE 5/10
    A63                715             492        68.8  BLK 501/513/508 ANG MO KIO STREET 52/53
    A64                132              77        58.3  BLK 584/586 ANG MO KIO STREET 51
    A65                 97              71        73.2  BLK 558/560 ANG MO KIO STREET 54
    A66                149              84        56.4  BLK 601/604/603 ANG MO KIO AVENUE 5
    A67                712             489        68.7  BLK 605/612 ANG MO KIO AVENUE 4/5
    A68                158              70        44.3  BLK 620/624/626 ANG MO KIO STREET 61
    A69                476             368        77.3  BLK 623/625/627 ANG MO KIO STREET 61
    A7                 238             183        76.9  BLK 212/213 ANG MO KIO STREET 23
    A70                134              57        42.5  BLK 629/626 ANG MO KIO AVENUE 4
    A71                185              56        30.3  BLK 628/632 ANG MO KIO STREET 61
    A72                358             239        66.8  BLK 633/640 ANG MO KIO STREET 61
    A73                414             119        28.7  BLK 641/645 ANG MO KIO STREET 61
    A74                185             118        63.8  BLK 646/649 ANG MO KIO STREET 61
    A75                354             247        69.8  BLK 177/182 ANG MO KIO AVENUE 4
    A76                818             662        80.9  BLK 613A ANG MO KIO AVENUE 4
    A77                267             172        64.4  BLK 150/156 ANG MO KIO AVENUE 5
    A78                546             323        59.2  BLK 157/163 ANG MO KIO AVENUE 4
    A8                  48              27        56.2  BLK 209/210 ANG MO KIO STREET 22
    A81                118              52        44.1  BLK 170/172 ANG MO KIO STREET 13
    A82                201             125        62.2  BLK 173/176 ANG MO KIO AVENUE 4
    A83                  -               -           -  BLK 5022 TO 5095 ANG MO KIO INDUSTRIAL PARK 2
    A85                 93              56        60.2  BLK 340 ANG MO KIO STREET 32
    A86                  -               -           -  BLK 4001-4003/4026-4028/4033-4035 ANG MO KIO INDUSTRIAL PARK 1
    A87                124              94        75.8  BLK 462/463 ANG MO KIO STREET 44
    A88                 44              26        59.1  BLK 348 ANG MO KIO AVENUE 3
    A89                  -               -           -  BLK 101/102 ANG MO KIO STREET 11
    A9                 146              77        52.7  BLK 202/203 ANG MO KIO STREET 22
    A90                  -               -           -  BLK 625/627 ANG MO KIO STREET 61
    A94                234             162        69.2  BLK 104C ANG MO KIO STREET 11
    A95                  -               -           -  BLK 323A ANG MO KIO AVENUE 3
    A98                108              79        73.1  BLK 259 ANG MO KIO AVENUE 2
    A99                  -               -           -  BLK 181 ANG MO KIO AVENUE 5
    Found 104 carparks matching 'ANG MO KIO'.
    ```

9.  ```
    Option 9: Display Carpark with the Most Parking Lots
    Carpark No  Carpark Type                     Parking System Type  Total Lots  Lots Available  Percentage  Address
    CKM5        MULTI-STOREY CAR PARK            ELECTRONIC PARKING         2754            2581        93.7  BLK 450A CHOA CHU KANG AVENUE 4
    ```

10. ```
    Option 10: Create an Output File with Carpark Availability with Addresses and Sort by Lots Available
    1933 lines written to 'carpark-availability-with-addresses.csv'.
    ```

    File output is in [carpark-availability-with-addresses.csv](carpark-availability-with-addresses.csv).
