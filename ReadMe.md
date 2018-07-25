# Paragon
Paragon Control Software:
this is an attempt to port the control software for the Ten-Tec Paragon written in MS Basic for the IBM 
PC to Python.

It uses a 1200 8N1 serial connection without hardware handshaking. 

It uses software timing loops for a 4.77Mhz processor in lines 2190 and 3150.

All keyboard functions of the Model 585 Paragon transceiver are controlled by sending codes in ASCII 
format to the Paragon. These codes correspond to the values located in the table. 

In the BASIC programming line:PRINT#1,D$. This must then be followed by GOSUB 2170, which calls a delay 
subroutine. This delay is required to allow the transceiver enough time to complete the requested 
operation before sending it another code. The delay routine is:FOR T = 1 TO 200; NEXT T: RETURN. This is
for a 4.77Mhz processor. For an IBM AT is reccomends increasing this loop to 500 or so.





<table>
	<tr>
	  <th>Key Function</td>
	  <th>Character</td>
	  <th>ASCII Code</td>
	</tr>
	<tr>
	  <td>0</td>
	  <td>0</td>
	  <td>30</td>
	</tr>
	<tr>
	  <td>1</td>
	  <td>1</td>
	  <td>31</td>
	</tr>
	<tr>
	  <td>2</td>
	  <td>2</td>
	  <td>32</td>
	</tr>
	<tr>
	  <td>3</td>
	  <td>3</td>
	  <td>33</td>
	</tr>
	<tr>
	  <td>4</td>
	  <td>4</td>
	  <td>34</td>
	</tr>
	<tr>
	  <td>5</td>
	  <td>5</td>
	  <td>35</td>
	</tr>
	<tr>
	  <td>6</td>
	  <td>6</td>
	  <td>36</td>
	</tr>
	<tr>
	  <td>7</td>
	  <td>7</td>
	  <td>37</td>
	</tr>
	<tr>
	  <td>8</td>
	  <td>8</td>
	  <td>38</td>
	</tr>
	<tr>
	  <td>9</td>
	  <td>9</td>
	  <td>39</td>
	</tr>
	<tr>
	  <td>RCL/GLC</td>
	  <td>:</td>
	  <td>3A</td>
	</tr>
	<tr>
	  <td>MLC/SET</td>
	  <td>;</td>
	  <td>3B</td>
	</tr>
	<tr>
	  <td>STO/GL</td>
	  <td><</td>
	  <td>3C</td>
	</tr>
	<tr>
	  <td>CLEAR</td>
	  <td>=</td>
	  <td>3D</td>
	</tr>
	<tr>
	  <td>VOICE</td>
	  <td>></td>
	  <td>3E</td>
	</tr>
	<tr>
	  <td>SPOT</td>
	  <td>?</td>
	  <td>3F</td>
	</tr>
	<tr>
	  <td>ENTER</td>
	  <td>@</td>
	  <td>40</td>
	</tr>
	<tr>
	  <td>MT/10HZ</td>
	  <td>A</td>
	  <td>41</td>
	</tr>
	<tr>
	  <td>DISP.></td>
	  <td>B</td>
	  <td>42</td>
	</tr>
	<tr>
	  <td>LCK</td>
	  <td>C</td>
	  <td>43</td>
	</tr>
	<tr>
	  <td>ML/MC</td>
	  <td>D</td>
	  <td>44</td>
	</tr>
	<tr>
	  <td>A=B</td>
	  <td>E</td>
	  <td>45</td>
	</tr>
	<tr>
	  <td>A/B</td>
	  <td>F</td>
	  <td>46</td>
	</tr>
	<tr>
	  <td>FAST</td>
	  <td>G</td>
	  <td>47</td>
	</tr>
	<tr>
	  <td>RX.OFF</td>
	  <td>G</td>
	  <td>48</td>
	</tr>
	<tr>
	  <td>TX.OFF</td>
	  <td>I</td>
	  <td>49</td>
	</tr>
	<tr>
	  <td>SPLIT</td>
	  <td>J</td>
	  <td>4A</td>
	</tr>
	<tr>
	  <td>MS/RATE</td>
	  <td>K</td>
	  <td>4B</td>
	</tr>
	<tr>
	  <td>FM</td>
	  <td>L</td>
	  <td>4C</td>
	</tr>
	<tr>
	  <td>AM</td>
	  <td>M</td>
	  <td>4D</td>
	</tr>
	<tr>
	  <td>LSB</td>
	  <td>N</td>
	  <td>1E</td>
	</tr>
	<tr>
	  <td>USB</td>
	  <td>O</td>
	  <td>1F</td>
	</tr>
	<tr>
	  <td>CW</td>
	  <td>P</td>
	  <td>50</td>
	</tr>
	<tr>
	  <td>TUNE</td>
	  <td>Q</td>
	  <td>51</td>
	</tr>
	<tr>
	  <td>6.0 Filter</td>
	  <td>R</td>
	  <td>52</td>
	</tr>
	<tr>
	  <td>2.4 Filter</td>
	  <td>S</td>
	  <td>53</td>
	</tr>
	<tr>
	  <td>1.8 Filter</td>
	  <td>T</td>
	  <td>54</td>
	</tr>
	<tr>
	  <td>.50 Filter</td>
	  <td>U</td>
	  <td>55</td>
	</tr>
	<tr>
	  <td>.25 Filter</td>
	  <td>V</td>
	  <td>56</td>
	</tr>
	<tr>
	  <td>.(DEC.PT).</td>
	  <td>W</td>
	  <td>57</td>
	</tr>
	<tr>
	  <td>SHIFT</td>
	  <td>X</td>
	  <td>58</td>
	</tr>
	<tr>
	  <td>DOWN/HBD</td>
	  <td>Y</td>
	  <td>59</td>
	</tr>
	<tr>
	  <td>UP/HBU</td>
	  <td>Z</td>
	  <td>5A</td>
	</tr>
	<tr>
	  <td>TUNE UP</td>
	  <td>[</td>
	  <td>5B</td>
	</tr>
	  <tr>
	  <td>STATUS</td>
	  <td>\</td>
	  <td>5C</td>
	</tr>
	<tr>
	  <td>TUNE DOWN</td>
	  <td>]</td>
	  <td>5D</td>
	</tr>
</table>
