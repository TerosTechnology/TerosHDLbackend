
# core: Integration

Module top is: core_top.vhd

## Schemas

![Module ports](./images/core_top_pkg.png)

## AXI interface

Example:

| OFFSET | LABEL              | R/W | SC  | DESCRIPTION        | RESET VALUE |
|:------:| ------------------ |:---:| --- | ------------------ | ----------- |
| 0x0000 | **core_VERSION**   |     |     |                    |             |
|        | *[31:0] Version*   |  R  | NO  | core version info. | VERSION     |
| 0x0004 | **core_CONFIG_ID** |     |     |                    |             |
|        | *[31:0] Config ID* |  R  | NO  | core Id Info.      | CONFIG_ID   |

### Memory mapped AXI interface.

Example:

| OFFSET | LABEL          | ELEMENTS    | R/W | SIZE | Type             | DESCRIPTION            | RESET VALUE |
|:------:| -------------- | ----------- | --- | ---- | ---------------- | ---------------------- | ----------- |
| 0x000C | **xxx_MEMORY** | NUM_WIN*512 |     |      | { struct }       | Memory of filter value | 0x10000000  |
|        | _[31:0] Data_  |             | W   | 4B   | Two's complement | dBm                    |             |

## Generic description table

| Generic         | Type    | Description                        | Tested values |
| --------------- | ------- | ---------------------------------- | ------------- |
| g_B10_SIZE_DATA | integer | Size of the processing data frames | [10:20]       |
| g_B2_SIZE_FFT   | integer | FFT size                           | [5:13]        |


```
generic (
  g_B10_BASEADDR        : integer :=  X;
  g_B10_AXI_ADDR_WIDTH  : integer := 32;
  g_B10_AXI_DAT_WIDTH   : integer := 32;
  g_B10_SIZE_MOD        : integer :=  9,10,11,12,13;
  g_B2_SIZE_FFT         : integer :=  5,6,7,8,9,10,11,12,13;
  g_B2_SIZE_PARALL      : integer :=  1;
  g_B10_ADI_ADDR_WIDTH  : integer :=  X;
  g_B10_ADI_DATA_WIDTH  : integer :=  X
);
```
- g_B10_BASEADDR: base10, dirección base.
- g_B2_SIZE_FFT: base2, tamaño de la FFT.
- g_B2_SIZE_PARALL: base2, número de paralelizaciones.

## Port description table

|    Port    | IN/OUT |                   Type                   | Description            |
|:----------:| ------ |:----------------------------------------:| ---------------------- |
| data_0_in  | in     | std_logic_vector(g_SIZE_DATA-1 downto 0) | data_0_in description  |
| data_1_out | out    | std_logic_vector(g_SIZE_DATA-1 downto 0) | data_1_out description |


## Other considerations


## Resources utilization

## Common errors
