#!/usr/bin/env python3
"""
Basic usage example for ReverseStrike
Demonstrates how to use the main modules
"""

from modules.packet_analyzer import PacketAnalyzer
from modules.port_scanner import PortScanner
from modules.vulnerability_scanner import VulnerabilityScanner

def main():
    print("=== ReverseStrike Basic Usage Example ===\n")
    
    # Example 1: Port Scanning
    print("1. Port Scanning Example:")
    scanner = PortScanner()
    open_ports = scanner.scan("example.com", start_port=70, end_port=90)
    print(f"   Open ports: {open_ports}\n")
    
    # Example 2: Packet Analysis
    print("2. Packet Analysis Example:")
    analyzer = PacketAnalyzer()
    packet_info = analyzer.analyze_pcap("sample.pcap")
    print(f"   Packet analysis: {packet_info}\n")
    
    # Example 3: Vulnerability Scanning
    print("3. Vulnerability Scanning Example:")
    vuln_scanner = VulnerabilityScanner()
    vulnerabilities = vuln_scanner.scan_target("192.168.1.1")
    print(f"   Found vulnerabilities: {len(vulnerabilities)}\n")
    
    print("Basic usage example completed!")

if __name__ == "__main__":
    main()
