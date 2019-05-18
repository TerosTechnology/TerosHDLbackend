-------------------------------------------------------
--! @file  core_top_tb.vhd
--! @brief sum calculation tb
--! @todo
--! @defgroup core
-------------------------------------------------------

--! Standard library.
library ieee;
--! Logic elements.
use ieee.std_logic_1164.all;
--! arithmetic functions.
use ieee.numeric_std.all;

--
library std;
use std.textio.all;
--
library src_lib;
use src_lib.core_top_pkg.all;

-- vunit
library vunit_lib;
context vunit_lib.vunit_context;

--! @brief   testbench
--! @details testbench of xxx
--! @ingroup core

entity core_top_tb is
  --vunit
  generic (runner_cfg : string);
end;

architecture bench of core_top_tb is
  -- clock period
  constant clk_period      : time := 5 ns;
  -- Signal ports
  signal clk   : std_logic;
  signal reset : std_logic;
  signal in_1  : std_logic_vector (4 downto 0);
  signal in_2  : std_logic_vector (4 downto 0);
  signal in_3  : std_logic_vector (4 downto 0);
  signal sum   : std_logic_vector (7 downto 0);


begin
  -- Instance
  core_top_i : core_top
  port map (
    clk   => clk,
    reset => reset,
    in_1  => in_1,
    in_2  => in_2,
    in_3  => in_3,
    sum   => sum
  );

  test_runner_watchdog(runner, 30 us);

  main : process
  begin
    test_runner_setup(runner, runner_cfg);
    while test_suite loop
      if run("test_alive") then
        logger_init(display_format => verbose);
          log("Test is alive");
        test_runner_cleanup(runner);

      elsif run("test_sum") then
        logger_init(display_format => verbose);
          wait for 2*clk_period;
          reset<='1';
          wait for 2*clk_period;
          reset<='0';
          in_1<=std_logic_vector(to_unsigned(3,5));
          in_2<=std_logic_vector(to_unsigned(4,5));
          in_3<=std_logic_vector(to_unsigned(9,5));
          wait for clk_period;
          check(unsigned(sum)=16,"Expect to pass so this should not be displayed");
        test_runner_cleanup(runner);

      elsif run("test_fail") then
          logger_init(display_format => verbose);
          log("Test fail");
          wait for 2*clk_period;
          check(1=2, "Expected to fail");
          test_runner_cleanup(runner);
      end if;
    end loop;
  end process;

  clk_process :process
  begin
    clk <= '1';
    wait for clk_period/2;
    clk <= '0';
    wait for clk_period/2;
  end process;

end;
