# orcs_4200_project
Muti-Armed Bandits RecSys (KuaiRec Dataset)

### KuaiRec Dataset

The KuaiRec Dataset contains user interactions on a webpage. 
For this project, we focus on the videos a user clicks. Our goal is to predict which video a user will click next, given the videos they clicked on in the past.

<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>user_id</th>
      <th>video_id</th>
      <th>play_duration</th>
      <th>video_duration</th>
      <th>time</th>
      <th>date</th>
      <th>timestamp</th>
      <th>watch_ratio</th>
      <th>first_level_category_id</th>
      <th>second_level_category_id</th>
      <th>third_level_category_id</th>
      <th>feat_1</th>
      <th>feat_2</th>
      <th>feat_3</th>
      <th>feat_4</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>14</td>
      <td>148</td>
      <td>4381</td>
      <td>6067</td>
      <td>97462.318</td>
      <td>20200705.0</td>
      <td>1.593898e+09</td>
      <td>0.722103</td>
      <td>19.0</td>
      <td>744.0</td>
      <td>2636.0</td>
      <td>11</td>
      <td>28.0</td>
      <td>19.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>14</td>
      <td>183</td>
      <td>11635</td>
      <td>6100</td>
      <td>97473.997</td>
      <td>20200705.0</td>
      <td>1.593898e+09</td>
      <td>1.907377</td>
      <td>28.0</td>
      <td>223.0</td>
      <td>-124.0</td>
      <td>28</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>14</td>
      <td>3649</td>
      <td>22422</td>
      <td>10867</td>
      <td>97543.419</td>
      <td>20200705.0</td>
      <td>1.593898e+09</td>
      <td>2.063311</td>
      <td>28.0</td>
      <td>223.0</td>
      <td>1830.0</td>
      <td>9</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>14</td>
      <td>5262</td>
      <td>4479</td>
      <td>7908</td>
      <td>97637.225</td>
      <td>20200705.0</td>
      <td>1.593898e+09</td>
      <td>0.566388</td>
      <td>5.0</td>
      <td>735.0</td>
      <td>-124.0</td>
      <td>25</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>14</td>
      <td>8234</td>
      <td>4602</td>
      <td>11000</td>
      <td>97937.399</td>
      <td>20200705.0</td>
      <td>1.593899e+09</td>
      <td>0.418364</td>
      <td>6.0</td>
      <td>667.0</td>
      <td>2375.0</td>
      <td>6</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>4676565</th>
      <td>7162</td>
      <td>2267</td>
      <td>11908</td>
      <td>5467</td>
      <td>2423337.210</td>
      <td>20200801.0</td>
      <td>1.596224e+09</td>
      <td>2.178160</td>
      <td>25.0</td>
      <td>235.0</td>
      <td>1272.0</td>
      <td>25</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>4676566</th>
      <td>7162</td>
      <td>2065</td>
      <td>11919</td>
      <td>6067</td>
      <td>2423337.210</td>
      <td>20200801.0</td>
      <td>1.596224e+09</td>
      <td>1.964562</td>
      <td>29.0</td>
      <td>689.0</td>
      <td>2455.0</td>
      <td>9</td>
      <td>17.0</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>4676567</th>
      <td>7162</td>
      <td>1296</td>
      <td>16690</td>
      <td>19870</td>
      <td>2423337.210</td>
      <td>20200801.0</td>
      <td>1.596224e+09</td>
      <td>0.839960</td>
      <td>1.0</td>
      <td>722.0</td>
      <td>2544.0</td>
      <td>1</td>
      <td>5.0</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>4676568</th>
      <td>7162</td>
      <td>4822</td>
      <td>11862</td>
      <td>24400</td>
      <td>2423337.210</td>
      <td>20200801.0</td>
      <td>1.596224e+09</td>
      <td>0.486148</td>
      <td>9.0</td>
      <td>136.0</td>
      <td>-124.0</td>
      <td>9</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>4676569</th>
      <td>7162</td>
      <td>4364</td>
      <td>2182</td>
      <td>19367</td>
      <td>2423337.210</td>
      <td>20200801.0</td>
      <td>1.596224e+09</td>
      <td>0.112666</td>
      <td>25.0</td>
      <td>235.0</td>
      <td>-124.0</td>
      <td>25</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
  </tbody>
</table>
<p>4676570 rows × 15 columns</p>
</div>

---

### Issues

The dataframe is too sparse (no user has watched every video on the website) and there are too many videos to choose from.

We resolve this by grouping each observation in the user interaction matrix by user, taking the sum of their watch ratio per catigory: 

```python
small_transformed_df = small_matrix_merged.pivot_table(index='user_id', 
                                           columns='first_level_category_id', 
                                           values='watch_ratio', 
                                           aggfunc='sum')  
```

<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th>first_level_category_id</th>
      <th>-124.0</th>
      <th>1.0</th>
      <th>2.0</th>
      <th>3.0</th>
      <th>4.0</th>
      <th>5.0</th>
      <th>6.0</th>
      <th>7.0</th>
      <th>8.0</th>
      <th>9.0</th>
      <th>...</th>
      <th>29.0</th>
      <th>31.0</th>
      <th>32.0</th>
      <th>33.0</th>
      <th>34.0</th>
      <th>35.0</th>
      <th>36.0</th>
      <th>37.0</th>
      <th>38.0</th>
      <th>39.0</th>
    </tr>
    <tr>
      <th>user_id</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>14</th>
      <td>4.286082</td>
      <td>143.114573</td>
      <td>18.780785</td>
      <td>3.990782</td>
      <td>23.204983</td>
      <td>127.466564</td>
      <td>226.189900</td>
      <td>154.046108</td>
      <td>274.076947</td>
      <td>104.960823</td>
      <td>...</td>
      <td>29.057355</td>
      <td>53.299769</td>
      <td>28.284356</td>
      <td>86.550536</td>
      <td>189.378020</td>
      <td>34.154832</td>
      <td>5.654891</td>
      <td>10.072252</td>
      <td>2.747260</td>
      <td>16.204715</td>
    </tr>
    <tr>
      <th>19</th>
      <td>2.181404</td>
      <td>114.764137</td>
      <td>15.067363</td>
      <td>4.878045</td>
      <td>26.105601</td>
      <td>110.512886</td>
      <td>184.396166</td>
      <td>125.246851</td>
      <td>260.217647</td>
      <td>91.961913</td>
      <td>...</td>
      <td>25.413421</td>
      <td>46.104619</td>
      <td>25.111988</td>
      <td>78.931972</td>
      <td>143.146660</td>
      <td>34.819603</td>
      <td>5.125674</td>
      <td>7.942315</td>
      <td>1.003059</td>
      <td>6.220014</td>
    </tr>
    <tr>
      <th>21</th>
      <td>2.926339</td>
      <td>124.110059</td>
      <td>23.230539</td>
      <td>5.624282</td>
      <td>27.482122</td>
      <td>130.194884</td>
      <td>240.155861</td>
      <td>142.008902</td>
      <td>289.964595</td>
      <td>93.602000</td>
      <td>...</td>
      <td>25.204688</td>
      <td>49.205301</td>
      <td>24.432978</td>
      <td>84.570179</td>
      <td>155.033386</td>
      <td>33.616927</td>
      <td>6.429626</td>
      <td>10.021961</td>
      <td>1.276294</td>
      <td>6.761944</td>
    </tr>
    <tr>
      <th>23</th>
      <td>3.981672</td>
      <td>107.067355</td>
      <td>26.635610</td>
      <td>6.181167</td>
      <td>20.649301</td>
      <td>131.889982</td>
      <td>191.524655</td>
      <td>154.143455</td>
      <td>317.001194</td>
      <td>124.566335</td>
      <td>...</td>
      <td>31.547009</td>
      <td>41.461490</td>
      <td>28.913310</td>
      <td>95.215205</td>
      <td>150.692951</td>
      <td>53.090773</td>
      <td>5.192854</td>
      <td>11.549175</td>
      <td>1.235337</td>
      <td>5.550794</td>
    </tr>
    <tr>
      <th>24</th>
      <td>2.684146</td>
      <td>89.313163</td>
      <td>13.462446</td>
      <td>5.342142</td>
      <td>26.527966</td>
      <td>132.614202</td>
      <td>178.508812</td>
      <td>113.466052</td>
      <td>323.619663</td>
      <td>91.335295</td>
      <td>...</td>
      <td>18.917689</td>
      <td>47.151678</td>
      <td>23.701717</td>
      <td>76.580128</td>
      <td>136.945069</td>
      <td>28.144926</td>
      <td>4.843280</td>
      <td>12.512766</td>
      <td>1.326224</td>
      <td>8.001600</td>
    </tr>
  </tbody>
</table>
<p>5 rows × 38 columns</p>
</div>

Lastly, we merge the features of each user (as one-hot encodings), to the above matrix.
This gives the user features and video watch ratios on each row:


```python
small_transformed_merged_df = (
    user_features
    .merge(small_transformed_df, on="user_id", how="right")
)
```

<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>const</th>
      <th>onehot_feat0</th>
      <th>onehot_feat1</th>
      <th>onehot_feat2</th>
      <th>onehot_feat3</th>
      <th>onehot_feat5</th>
      <th>onehot_feat6</th>
      <th>onehot_feat7</th>
      <th>onehot_feat8</th>
      <th>onehot_feat9</th>
      <th>...</th>
      <th>29.0</th>
      <th>31.0</th>
      <th>32.0</th>
      <th>33.0</th>
      <th>34.0</th>
      <th>35.0</th>
      <th>36.0</th>
      <th>37.0</th>
      <th>38.0</th>
      <th>39.0</th>
    </tr>
    <tr>
      <th>user_id</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>14</th>
      <td>1.0</td>
      <td>0</td>
      <td>5</td>
      <td>8</td>
      <td>417</td>
      <td>0</td>
      <td>1</td>
      <td>3</td>
      <td>297</td>
      <td>4</td>
      <td>...</td>
      <td>29.057355</td>
      <td>53.299769</td>
      <td>28.284356</td>
      <td>86.550536</td>
      <td>189.378020</td>
      <td>34.154832</td>
      <td>5.654891</td>
      <td>10.072252</td>
      <td>2.747260</td>
      <td>16.204715</td>
    </tr>
    <tr>
      <th>19</th>
      <td>1.0</td>
      <td>0</td>
      <td>1</td>
      <td>18</td>
      <td>589</td>
      <td>0</td>
      <td>1</td>
      <td>7</td>
      <td>227</td>
      <td>3</td>
      <td>...</td>
      <td>25.413421</td>
      <td>46.104619</td>
      <td>25.111988</td>
      <td>78.931972</td>
      <td>143.146660</td>
      <td>34.819603</td>
      <td>5.125674</td>
      <td>7.942315</td>
      <td>1.003059</td>
      <td>6.220014</td>
    </tr>
    <tr>
      <th>21</th>
      <td>1.0</td>
      <td>0</td>
      <td>4</td>
      <td>13</td>
      <td>568</td>
      <td>0</td>
      <td>0</td>
      <td>13</td>
      <td>292</td>
      <td>4</td>
      <td>...</td>
      <td>25.204688</td>
      <td>49.205301</td>
      <td>24.432978</td>
      <td>84.570179</td>
      <td>155.033386</td>
      <td>33.616927</td>
      <td>6.429626</td>
      <td>10.021961</td>
      <td>1.276294</td>
      <td>6.761944</td>
    </tr>
    <tr>
      <th>23</th>
      <td>1.0</td>
      <td>0</td>
      <td>1</td>
      <td>3</td>
      <td>45</td>
      <td>0</td>
      <td>0</td>
      <td>13</td>
      <td>148</td>
      <td>6</td>
      <td>...</td>
      <td>31.547009</td>
      <td>41.461490</td>
      <td>28.913310</td>
      <td>95.215205</td>
      <td>150.692951</td>
      <td>53.090773</td>
      <td>5.192854</td>
      <td>11.549175</td>
      <td>1.235337</td>
      <td>5.550794</td>
    </tr>
    <tr>
      <th>24</th>
      <td>1.0</td>
      <td>1</td>
      <td>4</td>
      <td>17</td>
      <td>634</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>64</td>
      <td>5</td>
      <td>...</td>
      <td>18.917689</td>
      <td>47.151678</td>
      <td>23.701717</td>
      <td>76.580128</td>
      <td>136.945069</td>
      <td>28.144926</td>
      <td>4.843280</td>
      <td>12.512766</td>
      <td>1.326224</td>
      <td>8.001600</td>
    </tr>
  </tbody>
</table>
<p>5 rows × 50 columns</p>
</div>

# Solution: LinUCB

Now we can formally define the problem with LinUCB:

$$
\begin{aligned}
\text{Arms: } & K           = 40 &\quad \text{The video catagory}\\
\text{Features: } & x_{t,a} \in \mathbb R^{11} &\quad \text{The user features}\\
\text{Reward Function: } & Reward_{t,a}  = x^\top_{t, a}\beta_a + \epsilon_{t,a}\\
\text{Objective: } & \min_{a_t} Regret_t  = \quad \sum_{t=1}^T(Reward_{t, a^*_t} - Reward_{t, a_t})
\end{aligned}
$$