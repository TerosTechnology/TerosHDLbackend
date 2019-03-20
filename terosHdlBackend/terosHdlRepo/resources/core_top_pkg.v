-------------------------------------------------------
--! @file  core_top_pkg.vhd
--! @brief Core package
--! @todo
--! @defgroup core
-------------------------------------------------------

--! Standard library.
library ieee;
--! Logic elements.
use ieee.std_logic_1164.all;
--! arithmetic functions.
use ieee.numeric_std.all;

--! @brief   package
--! @details package of xxx
--! @ingroup core

package core_top_pkg is

  component core_top is
    port (
      --# {{clocks|}}
      clk   : in  std_logic;
      --# {{user|user signals}}
      reset : in  std_logic;
      in_1  : in  std_logic_vector (4 downto 0);
      in_2  : in  std_logic_vector (4 downto 0);
      in_3  : in  std_logic_vector (4 downto 0);
      sum   : out std_logic_vector (7 downto 0)
      );
  end component;

end package;
