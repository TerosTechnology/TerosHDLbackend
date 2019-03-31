-------------------------------------------------------
--! @file  core_top.vhd
--! @brief sum calculation
--! @todo
--! @defgroup core
-------------------------------------------------------

--! Standard library.
library ieee;
--! Logic elements.
use ieee.std_logic_1164.all;
--! arithmetic functions.
use ieee.numeric_std.all;

--! @brief   implementation
--! @details implementation of xxx
--! @ingroup core

entity core_top is
  port (
         clk : in STD_LOGIC;
         reset: in STD_LOGIC;
         in_1 : in STD_LOGIC_VECTOR (4 downto 0);
         in_2 : in STD_LOGIC_VECTOR (4 downto 0);
         in_3 : in STD_LOGIC_VECTOR (4 downto 0);
         sum  : out STD_LOGIC_VECTOR (7 downto 0));
end core_top;

architecture rtl of core_top is

  --
  -- SIGNALS
  --

begin

  --
  -- CODE
  --

  process (clk)
  begin
     if (rising_edge(clk)) then
       if reset='1' then
         sum <= (OTHERS => '0');
       else
         sum <= "000" & std_logic_vector(unsigned(in_1)+unsigned(in_2)+ unsigned(in_3));
       end if;
     end if;
  end process;

end rtl;
