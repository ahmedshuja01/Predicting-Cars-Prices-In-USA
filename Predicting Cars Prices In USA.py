{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### Problem Statement\n",
    "A Chinese automobile company Geely Auto aspires to enter the US market by setting up their manufacturing unit there and producing cars locally to give competition to their US and European counterparts.\n",
    "\n",
    "They have contracted an automobile consulting company to understand the factors on which the pricing of cars depends. Specifically, they want to understand the factors affecting the pricing of cars in the American market, since those may be very different from the Chinese market. "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### Business Goal\n",
    "You are required to model the price of cars with the available independent variables. It will be used by the management to understand how exactly the prices vary with the independent variables. They can accordingly manipulate the design of the cars, the business strategy etc. to meet certain price levels. Further, the model will be a good way for management to understand the pricing dynamics of a new market."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "import matplotlib.pyplot as plt\n",
    "import seaborn as sns\n",
    "import numpy as np"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>car_ID</th>\n",
       "      <th>symboling</th>\n",
       "      <th>CarName</th>\n",
       "      <th>fueltype</th>\n",
       "      <th>aspiration</th>\n",
       "      <th>doornumber</th>\n",
       "      <th>carbody</th>\n",
       "      <th>drivewheel</th>\n",
       "      <th>enginelocation</th>\n",
       "      <th>wheelbase</th>\n",
       "      <th>...</th>\n",
       "      <th>enginesize</th>\n",
       "      <th>fuelsystem</th>\n",
       "      <th>boreratio</th>\n",
       "      <th>stroke</th>\n",
       "      <th>compressionratio</th>\n",
       "      <th>horsepower</th>\n",
       "      <th>peakrpm</th>\n",
       "      <th>citympg</th>\n",
       "      <th>highwaympg</th>\n",
       "      <th>price</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>1</td>\n",
       "      <td>3</td>\n",
       "      <td>alfa-romero giulia</td>\n",
       "      <td>gas</td>\n",
       "      <td>std</td>\n",
       "      <td>two</td>\n",
       "      <td>convertible</td>\n",
       "      <td>rwd</td>\n",
       "      <td>front</td>\n",
       "      <td>88.6</td>\n",
       "      <td>...</td>\n",
       "      <td>130</td>\n",
       "      <td>mpfi</td>\n",
       "      <td>3.47</td>\n",
       "      <td>2.68</td>\n",
       "      <td>9.0</td>\n",
       "      <td>111</td>\n",
       "      <td>5000</td>\n",
       "      <td>21</td>\n",
       "      <td>27</td>\n",
       "      <td>13495.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>2</td>\n",
       "      <td>3</td>\n",
       "      <td>alfa-romero stelvio</td>\n",
       "      <td>gas</td>\n",
       "      <td>std</td>\n",
       "      <td>two</td>\n",
       "      <td>convertible</td>\n",
       "      <td>rwd</td>\n",
       "      <td>front</td>\n",
       "      <td>88.6</td>\n",
       "      <td>...</td>\n",
       "      <td>130</td>\n",
       "      <td>mpfi</td>\n",
       "      <td>3.47</td>\n",
       "      <td>2.68</td>\n",
       "      <td>9.0</td>\n",
       "      <td>111</td>\n",
       "      <td>5000</td>\n",
       "      <td>21</td>\n",
       "      <td>27</td>\n",
       "      <td>16500.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>3</td>\n",
       "      <td>1</td>\n",
       "      <td>alfa-romero Quadrifoglio</td>\n",
       "      <td>gas</td>\n",
       "      <td>std</td>\n",
       "      <td>two</td>\n",
       "      <td>hatchback</td>\n",
       "      <td>rwd</td>\n",
       "      <td>front</td>\n",
       "      <td>94.5</td>\n",
       "      <td>...</td>\n",
       "      <td>152</td>\n",
       "      <td>mpfi</td>\n",
       "      <td>2.68</td>\n",
       "      <td>3.47</td>\n",
       "      <td>9.0</td>\n",
       "      <td>154</td>\n",
       "      <td>5000</td>\n",
       "      <td>19</td>\n",
       "      <td>26</td>\n",
       "      <td>16500.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>4</td>\n",
       "      <td>2</td>\n",
       "      <td>audi 100 ls</td>\n",
       "      <td>gas</td>\n",
       "      <td>std</td>\n",
       "      <td>four</td>\n",
       "      <td>sedan</td>\n",
       "      <td>fwd</td>\n",
       "      <td>front</td>\n",
       "      <td>99.8</td>\n",
       "      <td>...</td>\n",
       "      <td>109</td>\n",
       "      <td>mpfi</td>\n",
       "      <td>3.19</td>\n",
       "      <td>3.40</td>\n",
       "      <td>10.0</td>\n",
       "      <td>102</td>\n",
       "      <td>5500</td>\n",
       "      <td>24</td>\n",
       "      <td>30</td>\n",
       "      <td>13950.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>5</td>\n",
       "      <td>2</td>\n",
       "      <td>audi 100ls</td>\n",
       "      <td>gas</td>\n",
       "      <td>std</td>\n",
       "      <td>four</td>\n",
       "      <td>sedan</td>\n",
       "      <td>4wd</td>\n",
       "      <td>front</td>\n",
       "      <td>99.4</td>\n",
       "      <td>...</td>\n",
       "      <td>136</td>\n",
       "      <td>mpfi</td>\n",
       "      <td>3.19</td>\n",
       "      <td>3.40</td>\n",
       "      <td>8.0</td>\n",
       "      <td>115</td>\n",
       "      <td>5500</td>\n",
       "      <td>18</td>\n",
       "      <td>22</td>\n",
       "      <td>17450.0</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>5 rows × 26 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "   car_ID  symboling                   CarName fueltype aspiration doornumber  \\\n",
       "0       1          3        alfa-romero giulia      gas        std        two   \n",
       "1       2          3       alfa-romero stelvio      gas        std        two   \n",
       "2       3          1  alfa-romero Quadrifoglio      gas        std        two   \n",
       "3       4          2               audi 100 ls      gas        std       four   \n",
       "4       5          2                audi 100ls      gas        std       four   \n",
       "\n",
       "       carbody drivewheel enginelocation  wheelbase  ...  enginesize  \\\n",
       "0  convertible        rwd          front       88.6  ...         130   \n",
       "1  convertible        rwd          front       88.6  ...         130   \n",
       "2    hatchback        rwd          front       94.5  ...         152   \n",
       "3        sedan        fwd          front       99.8  ...         109   \n",
       "4        sedan        4wd          front       99.4  ...         136   \n",
       "\n",
       "   fuelsystem  boreratio  stroke compressionratio horsepower  peakrpm citympg  \\\n",
       "0        mpfi       3.47    2.68              9.0        111     5000      21   \n",
       "1        mpfi       3.47    2.68              9.0        111     5000      21   \n",
       "2        mpfi       2.68    3.47              9.0        154     5000      19   \n",
       "3        mpfi       3.19    3.40             10.0        102     5500      24   \n",
       "4        mpfi       3.19    3.40              8.0        115     5500      18   \n",
       "\n",
       "   highwaympg    price  \n",
       "0          27  13495.0  \n",
       "1          27  16500.0  \n",
       "2          26  16500.0  \n",
       "3          30  13950.0  \n",
       "4          22  17450.0  \n",
       "\n",
       "[5 rows x 26 columns]"
      ]
     },
     "execution_count": 2,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df=pd.read_csv('CarPrice_Assignment.csv')\n",
    "df.head(5)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'pandas.core.frame.DataFrame'>\n",
      "RangeIndex: 205 entries, 0 to 204\n",
      "Data columns (total 26 columns):\n",
      " #   Column            Non-Null Count  Dtype  \n",
      "---  ------            --------------  -----  \n",
      " 0   car_ID            205 non-null    int64  \n",
      " 1   symboling         205 non-null    int64  \n",
      " 2   CarName           205 non-null    object \n",
      " 3   fueltype          205 non-null    object \n",
      " 4   aspiration        205 non-null    object \n",
      " 5   doornumber        205 non-null    object \n",
      " 6   carbody           205 non-null    object \n",
      " 7   drivewheel        205 non-null    object \n",
      " 8   enginelocation    205 non-null    object \n",
      " 9   wheelbase         205 non-null    float64\n",
      " 10  carlength         205 non-null    float64\n",
      " 11  carwidth          205 non-null    float64\n",
      " 12  carheight         205 non-null    float64\n",
      " 13  curbweight        205 non-null    int64  \n",
      " 14  enginetype        205 non-null    object \n",
      " 15  cylindernumber    205 non-null    object \n",
      " 16  enginesize        205 non-null    int64  \n",
      " 17  fuelsystem        205 non-null    object \n",
      " 18  boreratio         205 non-null    float64\n",
      " 19  stroke            205 non-null    float64\n",
      " 20  compressionratio  205 non-null    float64\n",
      " 21  horsepower        205 non-null    int64  \n",
      " 22  peakrpm           205 non-null    int64  \n",
      " 23  citympg           205 non-null    int64  \n",
      " 24  highwaympg        205 non-null    int64  \n",
      " 25  price             205 non-null    float64\n",
      "dtypes: float64(8), int64(8), object(10)\n",
      "memory usage: 41.8+ KB\n"
     ]
    }
   ],
   "source": [
    "df.info()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### Summary of dataset "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>car_ID</th>\n",
       "      <th>symboling</th>\n",
       "      <th>wheelbase</th>\n",
       "      <th>carlength</th>\n",
       "      <th>carwidth</th>\n",
       "      <th>carheight</th>\n",
       "      <th>curbweight</th>\n",
       "      <th>enginesize</th>\n",
       "      <th>boreratio</th>\n",
       "      <th>stroke</th>\n",
       "      <th>compressionratio</th>\n",
       "      <th>horsepower</th>\n",
       "      <th>peakrpm</th>\n",
       "      <th>citympg</th>\n",
       "      <th>highwaympg</th>\n",
       "      <th>price</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>count</th>\n",
       "      <td>205.000000</td>\n",
       "      <td>205.000000</td>\n",
       "      <td>205.000000</td>\n",
       "      <td>205.000000</td>\n",
       "      <td>205.000000</td>\n",
       "      <td>205.000000</td>\n",
       "      <td>205.000000</td>\n",
       "      <td>205.000000</td>\n",
       "      <td>205.000000</td>\n",
       "      <td>205.000000</td>\n",
       "      <td>205.000000</td>\n",
       "      <td>205.000000</td>\n",
       "      <td>205.000000</td>\n",
       "      <td>205.000000</td>\n",
       "      <td>205.000000</td>\n",
       "      <td>205.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>mean</th>\n",
       "      <td>103.000000</td>\n",
       "      <td>0.834146</td>\n",
       "      <td>98.756585</td>\n",
       "      <td>174.049268</td>\n",
       "      <td>65.907805</td>\n",
       "      <td>53.724878</td>\n",
       "      <td>2555.565854</td>\n",
       "      <td>126.907317</td>\n",
       "      <td>3.329756</td>\n",
       "      <td>3.255415</td>\n",
       "      <td>10.142537</td>\n",
       "      <td>104.117073</td>\n",
       "      <td>5125.121951</td>\n",
       "      <td>25.219512</td>\n",
       "      <td>30.751220</td>\n",
       "      <td>13276.710571</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>std</th>\n",
       "      <td>59.322565</td>\n",
       "      <td>1.245307</td>\n",
       "      <td>6.021776</td>\n",
       "      <td>12.337289</td>\n",
       "      <td>2.145204</td>\n",
       "      <td>2.443522</td>\n",
       "      <td>520.680204</td>\n",
       "      <td>41.642693</td>\n",
       "      <td>0.270844</td>\n",
       "      <td>0.313597</td>\n",
       "      <td>3.972040</td>\n",
       "      <td>39.544167</td>\n",
       "      <td>476.985643</td>\n",
       "      <td>6.542142</td>\n",
       "      <td>6.886443</td>\n",
       "      <td>7988.852332</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>min</th>\n",
       "      <td>1.000000</td>\n",
       "      <td>-2.000000</td>\n",
       "      <td>86.600000</td>\n",
       "      <td>141.100000</td>\n",
       "      <td>60.300000</td>\n",
       "      <td>47.800000</td>\n",
       "      <td>1488.000000</td>\n",
       "      <td>61.000000</td>\n",
       "      <td>2.540000</td>\n",
       "      <td>2.070000</td>\n",
       "      <td>7.000000</td>\n",
       "      <td>48.000000</td>\n",
       "      <td>4150.000000</td>\n",
       "      <td>13.000000</td>\n",
       "      <td>16.000000</td>\n",
       "      <td>5118.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>25%</th>\n",
       "      <td>52.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>94.500000</td>\n",
       "      <td>166.300000</td>\n",
       "      <td>64.100000</td>\n",
       "      <td>52.000000</td>\n",
       "      <td>2145.000000</td>\n",
       "      <td>97.000000</td>\n",
       "      <td>3.150000</td>\n",
       "      <td>3.110000</td>\n",
       "      <td>8.600000</td>\n",
       "      <td>70.000000</td>\n",
       "      <td>4800.000000</td>\n",
       "      <td>19.000000</td>\n",
       "      <td>25.000000</td>\n",
       "      <td>7788.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>50%</th>\n",
       "      <td>103.000000</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>97.000000</td>\n",
       "      <td>173.200000</td>\n",
       "      <td>65.500000</td>\n",
       "      <td>54.100000</td>\n",
       "      <td>2414.000000</td>\n",
       "      <td>120.000000</td>\n",
       "      <td>3.310000</td>\n",
       "      <td>3.290000</td>\n",
       "      <td>9.000000</td>\n",
       "      <td>95.000000</td>\n",
       "      <td>5200.000000</td>\n",
       "      <td>24.000000</td>\n",
       "      <td>30.000000</td>\n",
       "      <td>10295.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>75%</th>\n",
       "      <td>154.000000</td>\n",
       "      <td>2.000000</td>\n",
       "      <td>102.400000</td>\n",
       "      <td>183.100000</td>\n",
       "      <td>66.900000</td>\n",
       "      <td>55.500000</td>\n",
       "      <td>2935.000000</td>\n",
       "      <td>141.000000</td>\n",
       "      <td>3.580000</td>\n",
       "      <td>3.410000</td>\n",
       "      <td>9.400000</td>\n",
       "      <td>116.000000</td>\n",
       "      <td>5500.000000</td>\n",
       "      <td>30.000000</td>\n",
       "      <td>34.000000</td>\n",
       "      <td>16503.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>max</th>\n",
       "      <td>205.000000</td>\n",
       "      <td>3.000000</td>\n",
       "      <td>120.900000</td>\n",
       "      <td>208.100000</td>\n",
       "      <td>72.300000</td>\n",
       "      <td>59.800000</td>\n",
       "      <td>4066.000000</td>\n",
       "      <td>326.000000</td>\n",
       "      <td>3.940000</td>\n",
       "      <td>4.170000</td>\n",
       "      <td>23.000000</td>\n",
       "      <td>288.000000</td>\n",
       "      <td>6600.000000</td>\n",
       "      <td>49.000000</td>\n",
       "      <td>54.000000</td>\n",
       "      <td>45400.000000</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "           car_ID   symboling   wheelbase   carlength    carwidth   carheight  \\\n",
       "count  205.000000  205.000000  205.000000  205.000000  205.000000  205.000000   \n",
       "mean   103.000000    0.834146   98.756585  174.049268   65.907805   53.724878   \n",
       "std     59.322565    1.245307    6.021776   12.337289    2.145204    2.443522   \n",
       "min      1.000000   -2.000000   86.600000  141.100000   60.300000   47.800000   \n",
       "25%     52.000000    0.000000   94.500000  166.300000   64.100000   52.000000   \n",
       "50%    103.000000    1.000000   97.000000  173.200000   65.500000   54.100000   \n",
       "75%    154.000000    2.000000  102.400000  183.100000   66.900000   55.500000   \n",
       "max    205.000000    3.000000  120.900000  208.100000   72.300000   59.800000   \n",
       "\n",
       "        curbweight  enginesize   boreratio      stroke  compressionratio  \\\n",
       "count   205.000000  205.000000  205.000000  205.000000        205.000000   \n",
       "mean   2555.565854  126.907317    3.329756    3.255415         10.142537   \n",
       "std     520.680204   41.642693    0.270844    0.313597          3.972040   \n",
       "min    1488.000000   61.000000    2.540000    2.070000          7.000000   \n",
       "25%    2145.000000   97.000000    3.150000    3.110000          8.600000   \n",
       "50%    2414.000000  120.000000    3.310000    3.290000          9.000000   \n",
       "75%    2935.000000  141.000000    3.580000    3.410000          9.400000   \n",
       "max    4066.000000  326.000000    3.940000    4.170000         23.000000   \n",
       "\n",
       "       horsepower      peakrpm     citympg  highwaympg         price  \n",
       "count  205.000000   205.000000  205.000000  205.000000    205.000000  \n",
       "mean   104.117073  5125.121951   25.219512   30.751220  13276.710571  \n",
       "std     39.544167   476.985643    6.542142    6.886443   7988.852332  \n",
       "min     48.000000  4150.000000   13.000000   16.000000   5118.000000  \n",
       "25%     70.000000  4800.000000   19.000000   25.000000   7788.000000  \n",
       "50%     95.000000  5200.000000   24.000000   30.000000  10295.000000  \n",
       "75%    116.000000  5500.000000   30.000000   34.000000  16503.000000  \n",
       "max    288.000000  6600.000000   49.000000   54.000000  45400.000000  "
      ]
     },
     "execution_count": 4,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.describe()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### Capture Only Company Name, not model"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>car_ID</th>\n",
       "      <th>symboling</th>\n",
       "      <th>manufacturing_company</th>\n",
       "      <th>fueltype</th>\n",
       "      <th>aspiration</th>\n",
       "      <th>doornumber</th>\n",
       "      <th>carbody</th>\n",
       "      <th>drivewheel</th>\n",
       "      <th>enginelocation</th>\n",
       "      <th>wheelbase</th>\n",
       "      <th>...</th>\n",
       "      <th>enginesize</th>\n",
       "      <th>fuelsystem</th>\n",
       "      <th>boreratio</th>\n",
       "      <th>stroke</th>\n",
       "      <th>compressionratio</th>\n",
       "      <th>horsepower</th>\n",
       "      <th>peakrpm</th>\n",
       "      <th>citympg</th>\n",
       "      <th>highwaympg</th>\n",
       "      <th>price</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>1</td>\n",
       "      <td>3</td>\n",
       "      <td>alfa-romero</td>\n",
       "      <td>gas</td>\n",
       "      <td>std</td>\n",
       "      <td>two</td>\n",
       "      <td>convertible</td>\n",
       "      <td>rwd</td>\n",
       "      <td>front</td>\n",
       "      <td>88.6</td>\n",
       "      <td>...</td>\n",
       "      <td>130</td>\n",
       "      <td>mpfi</td>\n",
       "      <td>3.47</td>\n",
       "      <td>2.68</td>\n",
       "      <td>9.0</td>\n",
       "      <td>111</td>\n",
       "      <td>5000</td>\n",
       "      <td>21</td>\n",
       "      <td>27</td>\n",
       "      <td>13495.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>2</td>\n",
       "      <td>3</td>\n",
       "      <td>alfa-romero</td>\n",
       "      <td>gas</td>\n",
       "      <td>std</td>\n",
       "      <td>two</td>\n",
       "      <td>convertible</td>\n",
       "      <td>rwd</td>\n",
       "      <td>front</td>\n",
       "      <td>88.6</td>\n",
       "      <td>...</td>\n",
       "      <td>130</td>\n",
       "      <td>mpfi</td>\n",
       "      <td>3.47</td>\n",
       "      <td>2.68</td>\n",
       "      <td>9.0</td>\n",
       "      <td>111</td>\n",
       "      <td>5000</td>\n",
       "      <td>21</td>\n",
       "      <td>27</td>\n",
       "      <td>16500.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>3</td>\n",
       "      <td>1</td>\n",
       "      <td>alfa-romero</td>\n",
       "      <td>gas</td>\n",
       "      <td>std</td>\n",
       "      <td>two</td>\n",
       "      <td>hatchback</td>\n",
       "      <td>rwd</td>\n",
       "      <td>front</td>\n",
       "      <td>94.5</td>\n",
       "      <td>...</td>\n",
       "      <td>152</td>\n",
       "      <td>mpfi</td>\n",
       "      <td>2.68</td>\n",
       "      <td>3.47</td>\n",
       "      <td>9.0</td>\n",
       "      <td>154</td>\n",
       "      <td>5000</td>\n",
       "      <td>19</td>\n",
       "      <td>26</td>\n",
       "      <td>16500.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>4</td>\n",
       "      <td>2</td>\n",
       "      <td>audi</td>\n",
       "      <td>gas</td>\n",
       "      <td>std</td>\n",
       "      <td>four</td>\n",
       "      <td>sedan</td>\n",
       "      <td>fwd</td>\n",
       "      <td>front</td>\n",
       "      <td>99.8</td>\n",
       "      <td>...</td>\n",
       "      <td>109</td>\n",
       "      <td>mpfi</td>\n",
       "      <td>3.19</td>\n",
       "      <td>3.40</td>\n",
       "      <td>10.0</td>\n",
       "      <td>102</td>\n",
       "      <td>5500</td>\n",
       "      <td>24</td>\n",
       "      <td>30</td>\n",
       "      <td>13950.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>5</td>\n",
       "      <td>2</td>\n",
       "      <td>audi</td>\n",
       "      <td>gas</td>\n",
       "      <td>std</td>\n",
       "      <td>four</td>\n",
       "      <td>sedan</td>\n",
       "      <td>4wd</td>\n",
       "      <td>front</td>\n",
       "      <td>99.4</td>\n",
       "      <td>...</td>\n",
       "      <td>136</td>\n",
       "      <td>mpfi</td>\n",
       "      <td>3.19</td>\n",
       "      <td>3.40</td>\n",
       "      <td>8.0</td>\n",
       "      <td>115</td>\n",
       "      <td>5500</td>\n",
       "      <td>18</td>\n",
       "      <td>22</td>\n",
       "      <td>17450.0</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>5 rows × 26 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "   car_ID  symboling manufacturing_company fueltype aspiration doornumber  \\\n",
       "0       1          3           alfa-romero      gas        std        two   \n",
       "1       2          3           alfa-romero      gas        std        two   \n",
       "2       3          1           alfa-romero      gas        std        two   \n",
       "3       4          2                  audi      gas        std       four   \n",
       "4       5          2                  audi      gas        std       four   \n",
       "\n",
       "       carbody drivewheel enginelocation  wheelbase  ...  enginesize  \\\n",
       "0  convertible        rwd          front       88.6  ...         130   \n",
       "1  convertible        rwd          front       88.6  ...         130   \n",
       "2    hatchback        rwd          front       94.5  ...         152   \n",
       "3        sedan        fwd          front       99.8  ...         109   \n",
       "4        sedan        4wd          front       99.4  ...         136   \n",
       "\n",
       "   fuelsystem  boreratio  stroke compressionratio horsepower  peakrpm citympg  \\\n",
       "0        mpfi       3.47    2.68              9.0        111     5000      21   \n",
       "1        mpfi       3.47    2.68              9.0        111     5000      21   \n",
       "2        mpfi       2.68    3.47              9.0        154     5000      19   \n",
       "3        mpfi       3.19    3.40             10.0        102     5500      24   \n",
       "4        mpfi       3.19    3.40              8.0        115     5500      18   \n",
       "\n",
       "   highwaympg    price  \n",
       "0          27  13495.0  \n",
       "1          27  16500.0  \n",
       "2          26  16500.0  \n",
       "3          30  13950.0  \n",
       "4          22  17450.0  \n",
       "\n",
       "[5 rows x 26 columns]"
      ]
     },
     "execution_count": 5,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "manufacturing_company=df['CarName'].apply(lambda x: x.split(' ')[0])\n",
    "df.insert(3,'manufacturing_company',manufacturing_company)\n",
    "df.drop('CarName',inplace=True,axis=1)\n",
    "df.head()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### Manufacturing Companies"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array(['alfa-romero', 'audi', 'bmw', 'chevrolet', 'dodge', 'honda',\n",
       "       'isuzu', 'jaguar', 'maxda', 'mazda', 'buick', 'mercury',\n",
       "       'mitsubishi', 'Nissan', 'nissan', 'peugeot', 'plymouth', 'porsche',\n",
       "       'porcshce', 'renault', 'saab', 'subaru', 'toyota', 'toyouta',\n",
       "       'vokswagen', 'volkswagen', 'vw', 'volvo'], dtype=object)"
      ]
     },
     "execution_count": 6,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df['manufacturing_company'].unique()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### Drivewheel"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array(['rwd', 'fwd', '4wd'], dtype=object)"
      ]
     },
     "execution_count": 7,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df['drivewheel'].unique()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### Cylinder number"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array(['four', 'six', 'five', 'three', 'twelve', 'two', 'eight'],\n",
       "      dtype=object)"
      ]
     },
     "execution_count": 8,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df['cylindernumber'].unique()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### Carbody"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 50,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array(['convertible', 'hatchback', 'sedan', 'wagon', 'hardtop'],\n",
       "      dtype=object)"
      ]
     },
     "execution_count": 50,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df['carbody'].unique()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### Enginelocation"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 51,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array(['front', 'rear'], dtype=object)"
      ]
     },
     "execution_count": 51,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df['enginelocation'].unique()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### Fuel type"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 52,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array(['gas', 'diesel'], dtype=object)"
      ]
     },
     "execution_count": 52,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df['fueltype'].unique()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### Door Number"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array(['two', 'four'], dtype=object)"
      ]
     },
     "execution_count": 9,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df['doornumber'].unique()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [],
   "source": [
    "df.replace('maxda','mazda',inplace=True)\n",
    "df.replace('porsche','porcshce',inplace=True)\n",
    "df.replace('nissan','Nissan',inplace=True)\n",
    "df.replace('toyouta','toyota',inplace=True)\n",
    "df.replace('vokswagen','volkswagen',inplace=True)\n",
    "df.replace('vw','volkswagen',inplace=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "car_ID                   0\n",
       "symboling                0\n",
       "manufacturing_company    0\n",
       "fueltype                 0\n",
       "aspiration               0\n",
       "doornumber               0\n",
       "carbody                  0\n",
       "drivewheel               0\n",
       "enginelocation           0\n",
       "wheelbase                0\n",
       "carlength                0\n",
       "carwidth                 0\n",
       "carheight                0\n",
       "curbweight               0\n",
       "enginetype               0\n",
       "cylindernumber           0\n",
       "enginesize               0\n",
       "fuelsystem               0\n",
       "boreratio                0\n",
       "stroke                   0\n",
       "compressionratio         0\n",
       "horsepower               0\n",
       "peakrpm                  0\n",
       "citympg                  0\n",
       "highwaympg               0\n",
       "price                    0\n",
       "dtype: int64"
      ]
     },
     "execution_count": 11,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Checking Null Values\n",
    "df.isnull().sum()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<seaborn.axisgrid.PairGrid at 0x1baab3e8340>"
      ]
     },
     "execution_count": 12,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 1620x180 with 10 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "sns.pairplot(\n",
    "    df,\n",
    "    x_vars=[\"price\", \"enginesize\", \"boreratio\",\"stroke\",\"compressionratio\",\"horsepower\",'wheelbase',\"citympg\",'highwaympg'],\n",
    "    y_vars=[\"price\"],\n",
    ")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "C:\\Users\\Ahmed\\anaconda3\\lib\\site-packages\\seaborn\\distributions.py:2551: FutureWarning: `distplot` is a deprecated function and will be removed in a future version. Please adapt your code to use either `displot` (a figure-level function with similar flexibility) or `histplot` (an axes-level function for histograms).\n",
      "  warnings.warn(msg, FutureWarning)\n",
      "C:\\Users\\Ahmed\\anaconda3\\lib\\site-packages\\seaborn\\distributions.py:2551: FutureWarning: `distplot` is a deprecated function and will be removed in a future version. Please adapt your code to use either `displot` (a figure-level function with similar flexibility) or `histplot` (an axes-level function for histograms).\n",
      "  warnings.warn(msg, FutureWarning)\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "<AxesSubplot:xlabel='wheelbase', ylabel='Density'>"
      ]
     },
     "execution_count": 13,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAAAYgAAAEGCAYAAAB/+QKOAAAAOXRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjMuMiwgaHR0cHM6Ly9tYXRwbG90bGliLm9yZy8vihELAAAACXBIWXMAAAsTAAALEwEAmpwYAABAB0lEQVR4nO3dd3hUVfrA8e87k947IYGQAKEXgdBFBcQCKra14+ruiqisu3bW8tPVdZXV1bXgKotl1cWCFZUiIAoqLUGkl0AogQAhJKTXOb8/ZnSzOGkwN5OE9/M882Ry77nnvLmQvHPvueccMcaglFJKHc/m7QCUUkq1TJoglFJKuaUJQimllFuaIJRSSrmlCUIppZRbPt4OwJNiYmJMcnKyt8NQSqlWIyMj44gxJtbdvjaVIJKTk0lPT/d2GEop1WqIyJ669uktJqWUUm5pglBKKeWWJgillFJuWZogROQ8EdkmIpkiMs3N/h4iskJEKkTkbjf77SLyg4h8bmWcSimlfsmyBCEidmAGcD7QC7haRHodV+wocDvwdB3V/AHYYlWMSiml6mblFcQQINMYs8sYUwm8C0ysXcAYc9gYswaoOv5gEekATABmWRijUkqpOliZIBKBfbW+z3Zta6x/APcCjvoKichkEUkXkfTc3NwmB6mUUso9KxOEuNnWqLnFReQC4LAxJqOhssaYmcaYNGNMWmys27EeSimlToCVCSIb6Fjr+w7AgUYeOxK4SER247w1NUZE3vZseEoppepj5UjqNUCqiKQA+4GrgGsac6Ax5k/AnwBE5CzgbmPMddaEqVqzVXP+ftJ1DP3VXR6IRKm2x7IEYYypFpGpwELADrxmjNkkIlNc+18WkXggHQgDHCLyR6CXMabQqriUUko1jqVzMRlj5gHzjtv2cq33B3Heeqqvjq+Bry0ITymlVD10JLVSSim3NEEopZRySxOEUkoptzRBKKWUcksThFJKKbc0QSillHJLE4RSSim3NEEopZRySxOEUkoptzRBKKWUcksThFJKKbc0QSillHJLE4RSSim3NEEopZRySxOEUkoptzRBKKWUcksThFJKKbc0QSillHJLE4RSSim3NEEopZRySxOEUkoptyxNECJynohsE5FMEZnmZn8PEVkhIhUicnet7R1FZKmIbBGRTSLyByvjVEop9Us+VlUsInZgBjAOyAbWiMhc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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "# removing outlier and making normal\n",
    "q = df['wheelbase'].quantile(0.96)\n",
    "df1 = df[df['wheelbase']<q]\n",
    "sns.distplot(df1['wheelbase'])\n",
    "\n",
    "import scipy.stats as ss \n",
    "sns.distplot(df1['wheelbase'],fit=ss.norm)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "C:\\Users\\Ahmed\\anaconda3\\lib\\site-packages\\seaborn\\distributions.py:2551: FutureWarning: `distplot` is a deprecated function and will be removed in a future version. Please adapt your code to use either `displot` (a figure-level function with similar flexibility) or `histplot` (an axes-level function for histograms).\n",
      "  warnings.warn(msg, FutureWarning)\n",
      "<ipython-input-15-4b1e35b8d741>:4: SettingWithCopyWarning: \n",
      "A value is trying to be set on a copy of a slice from a DataFrame.\n",
      "Try using .loc[row_indexer,col_indexer] = value instead\n",
      "\n",
      "See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy\n",
      "  df1['log_price'] = log_price\n"
     ]
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "# trasnform dependent variable \n",
    "log_price = np.log(df1['price'])\n",
    "sns.distplot(log_price)\n",
    "df1['log_price'] = log_price"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<seaborn.axisgrid.PairGrid at 0x1baabce1910>"
      ]
     },
     "execution_count": 16,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 1440x180 with 9 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "sns.pairplot(\n",
    "    df1,\n",
    "    x_vars=[\"log_price\", \"enginesize\", \"boreratio\",\"stroke\",\"compressionratio\",\"horsepower\",'wheelbase',\"citympg\"],\n",
    "    y_vars=[\"log_price\"],\n",
    ")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<seaborn.axisgrid.PairGrid at 0x1baabd66fa0>"
      ]
     },
     "execution_count": 17,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 1260x180 with 8 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "sns.pairplot(\n",
    "    df1,\n",
    "    x_vars=[\"log_price\", \"peakrpm\", \"curbweight\",\"carheight\",\"carwidth\",\"carlength\",'highwaympg'],\n",
    "    y_vars=[\"log_price\"],\n",
    ")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "C:\\Users\\Ahmed\\anaconda3\\lib\\site-packages\\pandas\\core\\frame.py:4163: SettingWithCopyWarning: \n",
      "A value is trying to be set on a copy of a slice from a DataFrame\n",
      "\n",
      "See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy\n",
      "  return super().drop(\n"
     ]
    }
   ],
   "source": [
    "df1.drop(['price'],axis=1,inplace=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "metadata": {},
   "outputs": [],
   "source": [
    "df1.drop(['car_ID'],axis=1,inplace=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>symboling</th>\n",
       "      <th>manufacturing_company</th>\n",
       "      <th>fueltype</th>\n",
       "      <th>aspiration</th>\n",
       "      <th>doornumber</th>\n",
       "      <th>carbody</th>\n",
       "      <th>drivewheel</th>\n",
       "      <th>enginelocation</th>\n",
       "      <th>wheelbase</th>\n",
       "      <th>carlength</th>\n",
       "      <th>...</th>\n",
       "      <th>enginesize</th>\n",
       "      <th>fuelsystem</th>\n",
       "      <th>boreratio</th>\n",
       "      <th>stroke</th>\n",
       "      <th>compressionratio</th>\n",
       "      <th>horsepower</th>\n",
       "      <th>peakrpm</th>\n",
       "      <th>citympg</th>\n",
       "      <th>highwaympg</th>\n",
       "      <th>log_price</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>3</td>\n",
       "      <td>alfa-romero</td>\n",
       "      <td>gas</td>\n",
       "      <td>std</td>\n",
       "      <td>two</td>\n",
       "      <td>convertible</td>\n",
       "      <td>rwd</td>\n",
       "      <td>front</td>\n",
       "      <td>88.6</td>\n",
       "      <td>168.8</td>\n",
       "      <td>...</td>\n",
       "      <td>130</td>\n",
       "      <td>mpfi</td>\n",
       "      <td>3.47</td>\n",
       "      <td>2.68</td>\n",
       "      <td>9.0</td>\n",
       "      <td>111</td>\n",
       "      <td>5000</td>\n",
       "      <td>21</td>\n",
       "      <td>27</td>\n",
       "      <td>9.510075</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>3</td>\n",
       "      <td>alfa-romero</td>\n",
       "      <td>gas</td>\n",
       "      <td>std</td>\n",
       "      <td>two</td>\n",
       "      <td>convertible</td>\n",
       "      <td>rwd</td>\n",
       "      <td>front</td>\n",
       "      <td>88.6</td>\n",
       "      <td>168.8</td>\n",
       "      <td>...</td>\n",
       "      <td>130</td>\n",
       "      <td>mpfi</td>\n",
       "      <td>3.47</td>\n",
       "      <td>2.68</td>\n",
       "      <td>9.0</td>\n",
       "      <td>111</td>\n",
       "      <td>5000</td>\n",
       "      <td>21</td>\n",
       "      <td>27</td>\n",
       "      <td>9.711116</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>1</td>\n",
       "      <td>alfa-romero</td>\n",
       "      <td>gas</td>\n",
       "      <td>std</td>\n",
       "      <td>two</td>\n",
       "      <td>hatchback</td>\n",
       "      <td>rwd</td>\n",
       "      <td>front</td>\n",
       "      <td>94.5</td>\n",
       "      <td>171.2</td>\n",
       "      <td>...</td>\n",
       "      <td>152</td>\n",
       "      <td>mpfi</td>\n",
       "      <td>2.68</td>\n",
       "      <td>3.47</td>\n",
       "      <td>9.0</td>\n",
       "      <td>154</td>\n",
       "      <td>5000</td>\n",
       "      <td>19</td>\n",
       "      <td>26</td>\n",
       "      <td>9.711116</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>2</td>\n",
       "      <td>audi</td>\n",
       "      <td>gas</td>\n",
       "      <td>std</td>\n",
       "      <td>four</td>\n",
       "      <td>sedan</td>\n",
       "      <td>fwd</td>\n",
       "      <td>front</td>\n",
       "      <td>99.8</td>\n",
       "      <td>176.6</td>\n",
       "      <td>...</td>\n",
       "      <td>109</td>\n",
       "      <td>mpfi</td>\n",
       "      <td>3.19</td>\n",
       "      <td>3.40</td>\n",
       "      <td>10.0</td>\n",
       "      <td>102</td>\n",
       "      <td>5500</td>\n",
       "      <td>24</td>\n",
       "      <td>30</td>\n",
       "      <td>9.543235</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>2</td>\n",
       "      <td>audi</td>\n",
       "      <td>gas</td>\n",
       "      <td>std</td>\n",
       "      <td>four</td>\n",
       "      <td>sedan</td>\n",
       "      <td>4wd</td>\n",
       "      <td>front</td>\n",
       "      <td>99.4</td>\n",
       "      <td>176.6</td>\n",
       "      <td>...</td>\n",
       "      <td>136</td>\n",
       "      <td>mpfi</td>\n",
       "      <td>3.19</td>\n",
       "      <td>3.40</td>\n",
       "      <td>8.0</td>\n",
       "      <td>115</td>\n",
       "      <td>5500</td>\n",
       "      <td>18</td>\n",
       "      <td>22</td>\n",
       "      <td>9.767095</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>...</th>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>191</th>\n",
       "      <td>-1</td>\n",
       "      <td>volvo</td>\n",
       "      <td>gas</td>\n",
       "      <td>std</td>\n",
       "      <td>four</td>\n",
       "      <td>sedan</td>\n",
       "      <td>rwd</td>\n",
       "      <td>front</td>\n",
       "      <td>109.1</td>\n",
       "      <td>188.8</td>\n",
       "      <td>...</td>\n",
       "      <td>141</td>\n",
       "      <td>mpfi</td>\n",
       "      <td>3.78</td>\n",
       "      <td>3.15</td>\n",
       "      <td>9.5</td>\n",
       "      <td>114</td>\n",
       "      <td>5400</td>\n",
       "      <td>23</td>\n",
       "      <td>28</td>\n",
       "      <td>9.731809</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>192</th>\n",
       "      <td>-1</td>\n",
       "      <td>volvo</td>\n",
       "      <td>gas</td>\n",
       "      <td>turbo</td>\n",
       "      <td>four</td>\n",
       "      <td>sedan</td>\n",
       "      <td>rwd</td>\n",
       "      <td>front</td>\n",
       "      <td>109.1</td>\n",
       "      <td>188.8</td>\n",
       "      <td>...</td>\n",
       "      <td>141</td>\n",
       "      <td>mpfi</td>\n",
       "      <td>3.78</td>\n",
       "      <td>3.15</td>\n",
       "      <td>8.7</td>\n",
       "      <td>160</td>\n",
       "      <td>5300</td>\n",
       "      <td>19</td>\n",
       "      <td>25</td>\n",
       "      <td>9.854560</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>193</th>\n",
       "      <td>-1</td>\n",
       "      <td>volvo</td>\n",
       "      <td>gas</td>\n",
       "      <td>std</td>\n",
       "      <td>four</td>\n",
       "      <td>sedan</td>\n",
       "      <td>rwd</td>\n",
       "      <td>front</td>\n",
       "      <td>109.1</td>\n",
       "      <td>188.8</td>\n",
       "      <td>...</td>\n",
       "      <td>173</td>\n",
       "      <td>mpfi</td>\n",
       "      <td>3.58</td>\n",
       "      <td>2.87</td>\n",
       "      <td>8.8</td>\n",
       "      <td>134</td>\n",
       "      <td>5500</td>\n",
       "      <td>18</td>\n",
       "      <td>23</td>\n",
       "      <td>9.975110</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>194</th>\n",
       "      <td>-1</td>\n",
       "      <td>volvo</td>\n",
       "      <td>diesel</td>\n",
       "      <td>turbo</td>\n",
       "      <td>four</td>\n",
       "      <td>sedan</td>\n",
       "      <td>rwd</td>\n",
       "      <td>front</td>\n",
       "      <td>109.1</td>\n",
       "      <td>188.8</td>\n",
       "      <td>...</td>\n",
       "      <td>145</td>\n",
       "      <td>idi</td>\n",
       "      <td>3.01</td>\n",
       "      <td>3.40</td>\n",
       "      <td>23.0</td>\n",
       "      <td>106</td>\n",
       "      <td>4800</td>\n",
       "      <td>26</td>\n",
       "      <td>27</td>\n",
       "      <td>10.019936</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>195</th>\n",
       "      <td>-1</td>\n",
       "      <td>volvo</td>\n",
       "      <td>gas</td>\n",
       "      <td>turbo</td>\n",
       "      <td>four</td>\n",
       "      <td>sedan</td>\n",
       "      <td>rwd</td>\n",
       "      <td>front</td>\n",
       "      <td>109.1</td>\n",
       "      <td>188.8</td>\n",
       "      <td>...</td>\n",
       "      <td>141</td>\n",
       "      <td>mpfi</td>\n",
       "      <td>3.78</td>\n",
       "      <td>3.15</td>\n",
       "      <td>9.5</td>\n",
       "      <td>114</td>\n",
       "      <td>5400</td>\n",
       "      <td>19</td>\n",
       "      <td>25</td>\n",
       "      <td>10.026811</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>196 rows × 25 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "     symboling manufacturing_company fueltype aspiration doornumber  \\\n",
       "0            3           alfa-romero      gas        std        two   \n",
       "1            3           alfa-romero      gas        std        two   \n",
       "2            1           alfa-romero      gas        std        two   \n",
       "3            2                  audi      gas        std       four   \n",
       "4            2                  audi      gas        std       four   \n",
       "..         ...                   ...      ...        ...        ...   \n",
       "191         -1                 volvo      gas        std       four   \n",
       "192         -1                 volvo      gas      turbo       four   \n",
       "193         -1                 volvo      gas        std       four   \n",
       "194         -1                 volvo   diesel      turbo       four   \n",
       "195         -1                 volvo      gas      turbo       four   \n",
       "\n",
       "         carbody drivewheel enginelocation  wheelbase  carlength  ...  \\\n",
       "0    convertible        rwd          front       88.6      168.8  ...   \n",
       "1    convertible        rwd          front       88.6      168.8  ...   \n",
       "2      hatchback        rwd          front       94.5      171.2  ...   \n",
       "3          sedan        fwd          front       99.8      176.6  ...   \n",
       "4          sedan        4wd          front       99.4      176.6  ...   \n",
       "..           ...        ...            ...        ...        ...  ...   \n",
       "191        sedan        rwd          front      109.1      188.8  ...   \n",
       "192        sedan        rwd          front      109.1      188.8  ...   \n",
       "193        sedan        rwd          front      109.1      188.8  ...   \n",
       "194        sedan        rwd          front      109.1      188.8  ...   \n",
       "195        sedan        rwd          front      109.1      188.8  ...   \n",
       "\n",
       "     enginesize  fuelsystem  boreratio stroke compressionratio  horsepower  \\\n",
       "0           130        mpfi       3.47   2.68              9.0         111   \n",
       "1           130        mpfi       3.47   2.68              9.0         111   \n",
       "2           152        mpfi       2.68   3.47              9.0         154   \n",
       "3           109        mpfi       3.19   3.40             10.0         102   \n",
       "4           136        mpfi       3.19   3.40              8.0         115   \n",
       "..          ...         ...        ...    ...              ...         ...   \n",
       "191         141        mpfi       3.78   3.15              9.5         114   \n",
       "192         141        mpfi       3.78   3.15              8.7         160   \n",
       "193         173        mpfi       3.58   2.87              8.8         134   \n",
       "194         145         idi       3.01   3.40             23.0         106   \n",
       "195         141        mpfi       3.78   3.15              9.5         114   \n",
       "\n",
       "    peakrpm  citympg  highwaympg  log_price  \n",
       "0      5000       21          27   9.510075  \n",
       "1      5000       21          27   9.711116  \n",
       "2      5000       19          26   9.711116  \n",
       "3      5500       24          30   9.543235  \n",
       "4      5500       18          22   9.767095  \n",
       "..      ...      ...         ...        ...  \n",
       "191    5400       23          28   9.731809  \n",
       "192    5300       19          25   9.854560  \n",
       "193    5500       18          23   9.975110  \n",
       "194    4800       26          27  10.019936  \n",
       "195    5400       19          25  10.026811  \n",
       "\n",
       "[196 rows x 25 columns]"
      ]
     },
     "execution_count": 20,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df3= df1.reset_index(drop=True)\n",
    "df3"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "###  Checking Multicollinearity\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<AxesSubplot:>"
      ]
     },
     "execution_count": 21,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 2 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "sns.heatmap(df3.corr(),linewidths=.5)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "metadata": {},
   "outputs": [],
   "source": [
    "df3.drop(['citympg','highwaympg','symboling','peakrpm'],axis=1,inplace=True)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<AxesSubplot:>"
      ]
     },
     "execution_count": 24,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 2 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "sns.heatmap(df3.corr(),linewidths=.5)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Checking Null Values\n",
    "df3.isnull().sum()\n",
    "df6= df3.dropna(axis=0)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Create dummy variables"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "metadata": {},
   "outputs": [],
   "source": [
    "# To include the categorical data in the regression, let's create dummies\n",
    "# There is a very convenient method called: 'get_dummies' which does that seemlessly\n",
    "# It is extremely important that we drop one of the dummies, alternatively we will introduce multicollinearity\n",
    "data_with_dummies = pd.get_dummies(df6, drop_first=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>wheelbase</th>\n",
       "      <th>carlength</th>\n",
       "      <th>carwidth</th>\n",
       "      <th>carheight</th>\n",
       "      <th>curbweight</th>\n",
       "      <th>enginesize</th>\n",
       "      <th>boreratio</th>\n",
       "      <th>stroke</th>\n",
       "      <th>compressionratio</th>\n",
       "      <th>horsepower</th>\n",
       "      <th>...</th>\n",
       "      <th>cylindernumber_three</th>\n",
       "      <th>cylindernumber_twelve</th>\n",
       "      <th>cylindernumber_two</th>\n",
       "      <th>fuelsystem_2bbl</th>\n",
       "      <th>fuelsystem_4bbl</th>\n",
       "      <th>fuelsystem_idi</th>\n",
       "      <th>fuelsystem_mfi</th>\n",
       "      <th>fuelsystem_mpfi</th>\n",
       "      <th>fuelsystem_spdi</th>\n",
       "      <th>fuelsystem_spfi</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>88.6</td>\n",
       "      <td>168.8</td>\n",
       "      <td>64.1</td>\n",
       "      <td>48.8</td>\n",
       "      <td>2548</td>\n",
       "      <td>130</td>\n",
       "      <td>3.47</td>\n",
       "      <td>2.68</td>\n",
       "      <td>9.0</td>\n",
       "      <td>111</td>\n",
       "      <td>...</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>88.6</td>\n",
       "      <td>168.8</td>\n",
       "      <td>64.1</td>\n",
       "      <td>48.8</td>\n",
       "      <td>2548</td>\n",
       "      <td>130</td>\n",
       "      <td>3.47</td>\n",
       "      <td>2.68</td>\n",
       "      <td>9.0</td>\n",
       "      <td>111</td>\n",
       "      <td>...</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>94.5</td>\n",
       "      <td>171.2</td>\n",
       "      <td>65.5</td>\n",
       "      <td>52.4</td>\n",
       "      <td>2823</td>\n",
       "      <td>152</td>\n",
       "      <td>2.68</td>\n",
       "      <td>3.47</td>\n",
       "      <td>9.0</td>\n",
       "      <td>154</td>\n",
       "      <td>...</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>99.8</td>\n",
       "      <td>176.6</td>\n",
       "      <td>66.2</td>\n",
       "      <td>54.3</td>\n",
       "      <td>2337</td>\n",
       "      <td>109</td>\n",
       "      <td>3.19</td>\n",
       "      <td>3.40</td>\n",
       "      <td>10.0</td>\n",
       "      <td>102</td>\n",
       "      <td>...</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>99.4</td>\n",
       "      <td>176.6</td>\n",
       "      <td>66.4</td>\n",
       "      <td>54.3</td>\n",
       "      <td>2824</td>\n",
       "      <td>136</td>\n",
       "      <td>3.19</td>\n",
       "      <td>3.40</td>\n",
       "      <td>8.0</td>\n",
       "      <td>115</td>\n",
       "      <td>...</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>5 rows × 61 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "   wheelbase  carlength  carwidth  carheight  curbweight  enginesize  \\\n",
       "0       88.6      168.8      64.1       48.8        2548         130   \n",
       "1       88.6      168.8      64.1       48.8        2548         130   \n",
       "2       94.5      171.2      65.5       52.4        2823         152   \n",
       "3       99.8      176.6      66.2       54.3        2337         109   \n",
       "4       99.4      176.6      66.4       54.3        2824         136   \n",
       "\n",
       "   boreratio  stroke  compressionratio  horsepower  ...  cylindernumber_three  \\\n",
       "0       3.47    2.68               9.0         111  ...                     0   \n",
       "1       3.47    2.68               9.0         111  ...                     0   \n",
       "2       2.68    3.47               9.0         154  ...                     0   \n",
       "3       3.19    3.40              10.0         102  ...                     0   \n",
       "4       3.19    3.40               8.0         115  ...                     0   \n",
       "\n",
       "   cylindernumber_twelve  cylindernumber_two  fuelsystem_2bbl  \\\n",
       "0                      0                   0                0   \n",
       "1                      0                   0                0   \n",
       "2                      0                   0                0   \n",
       "3                      0                   0                0   \n",
       "4                      0                   0                0   \n",
       "\n",
       "   fuelsystem_4bbl  fuelsystem_idi  fuelsystem_mfi  fuelsystem_mpfi  \\\n",
       "0                0               0               0                1   \n",
       "1                0               0               0                1   \n",
       "2                0               0               0                1   \n",
       "3                0               0               0                1   \n",
       "4                0               0               0                1   \n",
       "\n",
       "   fuelsystem_spdi  fuelsystem_spfi  \n",
       "0                0                0  \n",
       "1                0                0  \n",
       "2                0                0  \n",
       "3                0                0  \n",
       "4                0                0  \n",
       "\n",
       "[5 rows x 61 columns]"
      ]
     },
     "execution_count": 27,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Here's the result\n",
    "data_with_dummies.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array(['wheelbase', 'carlength', 'carwidth', 'carheight', 'curbweight',\n",
       "       'enginesize', 'boreratio', 'stroke', 'compressionratio',\n",
       "       'horsepower', 'log_price', 'manufacturing_company_alfa-romero',\n",
       "       'manufacturing_company_audi', 'manufacturing_company_bmw',\n",
       "       'manufacturing_company_buick', 'manufacturing_company_chevrolet',\n",
       "       'manufacturing_company_dodge', 'manufacturing_company_honda',\n",
       "       'manufacturing_company_isuzu', 'manufacturing_company_jaguar',\n",
       "       'manufacturing_company_mazda', 'manufacturing_company_mercury',\n",
       "       'manufacturing_company_mitsubishi',\n",
       "       'manufacturing_company_peugeot', 'manufacturing_company_plymouth',\n",
       "       'manufacturing_company_porcshce', 'manufacturing_company_renault',\n",
       "       'manufacturing_company_saab', 'manufacturing_company_subaru',\n",
       "       'manufacturing_company_toyota', 'manufacturing_company_volkswagen',\n",
       "       'manufacturing_company_volvo', 'fueltype_gas', 'aspiration_turbo',\n",
       "       'doornumber_two', 'carbody_hardtop', 'carbody_hatchback',\n",
       "       'carbody_sedan', 'carbody_wagon', 'drivewheel_fwd',\n",
       "       'drivewheel_rwd', 'enginelocation_rear', 'enginetype_dohcv',\n",
       "       'enginetype_l', 'enginetype_ohc', 'enginetype_ohcf',\n",
       "       'enginetype_ohcv', 'enginetype_rotor', 'cylindernumber_five',\n",
       "       'cylindernumber_four', 'cylindernumber_six',\n",
       "       'cylindernumber_three', 'cylindernumber_twelve',\n",
       "       'cylindernumber_two', 'fuelsystem_2bbl', 'fuelsystem_4bbl',\n",
       "       'fuelsystem_idi', 'fuelsystem_mfi', 'fuelsystem_mpfi',\n",
       "       'fuelsystem_spdi', 'fuelsystem_spfi'], dtype=object)"
      ]
     },
     "execution_count": 28,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# To make our data frame more organized, we prefer to place the dependent variable in the beginning of the df\n",
    "# Since each problem is different, that must be done manually\n",
    "# We can display all possible features and then choose the desired order\n",
    "data_with_dummies.columns.values"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "metadata": {},
   "outputs": [],
   "source": [
    "cols=['wheelbase', 'carlength', 'carwidth', 'carheight', 'curbweight',\n",
    "       'enginesize', 'boreratio', 'stroke', 'compressionratio',\n",
    "       'horsepower', 'manufacturing_company_alfa-romero',\n",
    "       'manufacturing_company_audi', 'manufacturing_company_bmw',\n",
    "       'manufacturing_company_buick', 'manufacturing_company_chevrolet',\n",
    "       'manufacturing_company_dodge', 'manufacturing_company_honda',\n",
    "       'manufacturing_company_isuzu', 'manufacturing_company_jaguar',\n",
    "       'manufacturing_company_mazda', 'manufacturing_company_mercury',\n",
    "       'manufacturing_company_mitsubishi',\n",
    "       'manufacturing_company_peugeot', 'manufacturing_company_plymouth',\n",
    "       'manufacturing_company_porcshce', 'manufacturing_company_renault',\n",
    "       'manufacturing_company_saab', 'manufacturing_company_subaru',\n",
    "       'manufacturing_company_toyota', 'manufacturing_company_volkswagen',\n",
    "       'manufacturing_company_volvo', 'fueltype_gas', 'aspiration_turbo',\n",
    "       'doornumber_two', 'carbody_hardtop', 'carbody_hatchback',\n",
    "       'carbody_sedan', 'carbody_wagon', 'drivewheel_fwd',\n",
    "       'drivewheel_rwd', 'enginelocation_rear', 'enginetype_dohcv',\n",
    "       'enginetype_l', 'enginetype_ohc', 'enginetype_ohcf',\n",
    "       'enginetype_ohcv', 'enginetype_rotor', 'cylindernumber_five',\n",
    "       'cylindernumber_four', 'cylindernumber_six',\n",
    "       'cylindernumber_three', 'cylindernumber_twelve',\n",
    "       'cylindernumber_two', 'fuelsystem_2bbl', 'fuelsystem_4bbl',\n",
    "       'fuelsystem_idi', 'fuelsystem_mfi', 'fuelsystem_mpfi',\n",
    "       'fuelsystem_spdi', 'fuelsystem_spfi','log_price']"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>wheelbase</th>\n",
       "      <th>carlength</th>\n",
       "      <th>carwidth</th>\n",
       "      <th>carheight</th>\n",
       "      <th>curbweight</th>\n",
       "      <th>enginesize</th>\n",
       "      <th>boreratio</th>\n",
       "      <th>stroke</th>\n",
       "      <th>compressionratio</th>\n",
       "      <th>horsepower</th>\n",
       "      <th>...</th>\n",
       "      <th>cylindernumber_twelve</th>\n",
       "      <th>cylindernumber_two</th>\n",
       "      <th>fuelsystem_2bbl</th>\n",
       "      <th>fuelsystem_4bbl</th>\n",
       "      <th>fuelsystem_idi</th>\n",
       "      <th>fuelsystem_mfi</th>\n",
       "      <th>fuelsystem_mpfi</th>\n",
       "      <th>fuelsystem_spdi</th>\n",
       "      <th>fuelsystem_spfi</th>\n",
       "      <th>log_price</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>88.6</td>\n",
       "      <td>168.8</td>\n",
       "      <td>64.1</td>\n",
       "      <td>48.8</td>\n",
       "      <td>2548</td>\n",
       "      <td>130</td>\n",
       "      <td>3.47</td>\n",
       "      <td>2.68</td>\n",
       "      <td>9.0</td>\n",
       "      <td>111</td>\n",
       "      <td>...</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>9.510075</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>88.6</td>\n",
       "      <td>168.8</td>\n",
       "      <td>64.1</td>\n",
       "      <td>48.8</td>\n",
       "      <td>2548</td>\n",
       "      <td>130</td>\n",
       "      <td>3.47</td>\n",
       "      <td>2.68</td>\n",
       "      <td>9.0</td>\n",
       "      <td>111</td>\n",
       "      <td>...</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>9.711116</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>94.5</td>\n",
       "      <td>171.2</td>\n",
       "      <td>65.5</td>\n",
       "      <td>52.4</td>\n",
       "      <td>2823</td>\n",
       "      <td>152</td>\n",
       "      <td>2.68</td>\n",
       "      <td>3.47</td>\n",
       "      <td>9.0</td>\n",
       "      <td>154</td>\n",
       "      <td>...</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>9.711116</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>99.8</td>\n",
       "      <td>176.6</td>\n",
       "      <td>66.2</td>\n",
       "      <td>54.3</td>\n",
       "      <td>2337</td>\n",
       "      <td>109</td>\n",
       "      <td>3.19</td>\n",
       "      <td>3.40</td>\n",
       "      <td>10.0</td>\n",
       "      <td>102</td>\n",
       "      <td>...</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>9.543235</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>99.4</td>\n",
       "      <td>176.6</td>\n",
       "      <td>66.4</td>\n",
       "      <td>54.3</td>\n",
       "      <td>2824</td>\n",
       "      <td>136</td>\n",
       "      <td>3.19</td>\n",
       "      <td>3.40</td>\n",
       "      <td>8.0</td>\n",
       "      <td>115</td>\n",
       "      <td>...</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>9.767095</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>5 rows × 61 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "   wheelbase  carlength  carwidth  carheight  curbweight  enginesize  \\\n",
       "0       88.6      168.8      64.1       48.8        2548         130   \n",
       "1       88.6      168.8      64.1       48.8        2548         130   \n",
       "2       94.5      171.2      65.5       52.4        2823         152   \n",
       "3       99.8      176.6      66.2       54.3        2337         109   \n",
       "4       99.4      176.6      66.4       54.3        2824         136   \n",
       "\n",
       "   boreratio  stroke  compressionratio  horsepower  ...  \\\n",
       "0       3.47    2.68               9.0         111  ...   \n",
       "1       3.47    2.68               9.0         111  ...   \n",
       "2       2.68    3.47               9.0         154  ...   \n",
       "3       3.19    3.40              10.0         102  ...   \n",
       "4       3.19    3.40               8.0         115  ...   \n",
       "\n",
       "   cylindernumber_twelve  cylindernumber_two  fuelsystem_2bbl  \\\n",
       "0                      0                   0                0   \n",
       "1                      0                   0                0   \n",
       "2                      0                   0                0   \n",
       "3                      0                   0                0   \n",
       "4                      0                   0                0   \n",
       "\n",
       "   fuelsystem_4bbl  fuelsystem_idi  fuelsystem_mfi  fuelsystem_mpfi  \\\n",
       "0                0               0               0                1   \n",
       "1                0               0               0                1   \n",
       "2                0               0               0                1   \n",
       "3                0               0               0                1   \n",
       "4                0               0               0                1   \n",
       "\n",
       "   fuelsystem_spdi  fuelsystem_spfi  log_price  \n",
       "0                0                0   9.510075  \n",
       "1                0                0   9.711116  \n",
       "2                0                0   9.711116  \n",
       "3                0                0   9.543235  \n",
       "4                0                0   9.767095  \n",
       "\n",
       "[5 rows x 61 columns]"
      ]
     },
     "execution_count": 31,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# To implement the reordering, we will create a new df, which is equal to the old one but with the new order of features\n",
    "data_preprocessed = data_with_dummies[cols]\n",
    "data_preprocessed.head()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Linear regression model"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Declare the inputs and the targets"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 32,
   "metadata": {},
   "outputs": [],
   "source": [
    "# The target(s) (dependent variable) is 'log price'\n",
    "targets = data_preprocessed['log_price']\n",
    "\n",
    "# The inputs are everything BUT the dependent variable, so we can simply drop it\n",
    "inputs = data_preprocessed.drop(['log_price'],axis=1)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Feature Scaling"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 33,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "StandardScaler()"
      ]
     },
     "execution_count": 33,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Import the scaling module\n",
    "from sklearn.preprocessing import StandardScaler\n",
    "\n",
    "# Create a scaler object\n",
    "scaler = StandardScaler()\n",
    "# Fit the inputs (calculate the mean and standard deviation feature-wise)\n",
    "scaler.fit(inputs)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 34,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Scale the features and store them in a new variable (the actual scaling procedure)\n",
    "inputs_scaled = scaler.transform(inputs)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Train / Test Split"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 35,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Import the module for the split\n",
    "from sklearn.model_selection import train_test_split\n",
    "\n",
    "# Split the variables with an 80-20 split and some random state\n",
    "x_train, x_test, y_train, y_test = train_test_split(inputs_scaled, targets, test_size=0.2, random_state=365)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 36,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "LinearRegression()"
      ]
     },
     "execution_count": 36,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "from sklearn.linear_model import LinearRegression\n",
    "# Create a linear regression object\n",
    "reg = LinearRegression()\n",
    "# Fit the regression with the scaled TRAIN inputs and targets\n",
    "reg.fit(x_train,y_train)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 37,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Let's check the outputs of the regression\n",
    "# I'll store them in y_hat as this is the 'theoretical' name of the predictions\n",
    "y_hat = reg.predict(x_train)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 38,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "# The simplest way to compare the targets (y_train) and the predictions (y_hat) is to plot them on a scatter plot\n",
    "# The closer the points to the 45-degree line, the better the prediction\n",
    "plt.scatter(y_train, y_hat)\n",
    "# Let's also name the axes\n",
    "plt.xlabel('Targets (y_train)',size=15)\n",
    "plt.ylabel('Predictions (y_hat)',size=15)\n",
    "plt.xlim(8,11)\n",
    "plt.ylim(8,11.5)\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 39,
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "C:\\Users\\Ahmed\\anaconda3\\lib\\site-packages\\seaborn\\distributions.py:2551: FutureWarning: `distplot` is a deprecated function and will be removed in a future version. Please adapt your code to use either `displot` (a figure-level function with similar flexibility) or `histplot` (an axes-level function for histograms).\n",
      "  warnings.warn(msg, FutureWarning)\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "Text(0.5, 1.0, 'Residuals PDF')"
      ]
     },
     "execution_count": 39,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "sns.distplot(y_train - y_hat)\n",
    "# Include a title\n",
    "plt.title(\"Residuals PDF\", size=16)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "**R^2 Square score**"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 40,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0.9604092300756217"
      ]
     },
     "execution_count": 40,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "reg.score(x_train,y_train)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 41,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "9.32321196865329"
      ]
     },
     "execution_count": 41,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "reg.intercept_"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 42,
   "metadata": {},
   "outputs": [],
   "source": [
    "# If the predictions are far off, we will know that our model overfitted\n",
    "y_hat_test = reg.predict(x_test)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 43,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "# Create a scatter plot with the test targets and the test predictions\n",
    "# You can include the argument 'alpha' which will introduce opacity to the graph\n",
    "plt.scatter(y_test, y_hat_test)\n",
    "plt.xlabel('Targets (y_test)',size=14)\n",
    "plt.ylabel('Predictions (y_hat_test)',size=14)\n",
    "plt.xlim(8,11)\n",
    "plt.ylim(8,11)\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Performance Metrics: RMSE "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 44,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0.1250301679660677"
      ]
     },
     "execution_count": 44,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "from sklearn import metrics\n",
    "np.sqrt(metrics.mean_squared_error(y_test,y_hat_test))"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python [conda env:base] *",
   "language": "python",
   "name": "conda-base-py"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
